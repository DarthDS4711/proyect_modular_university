import json
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from config.stripe.secret_keys_payment import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from core.product.models import Product, Size
from core.stock.models import Stock, StockProductSize
from core.sale.models import DetailSale, Sale
from core.user.models import DirectionUser


class ShopCartView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = "shopCart.html"
    login_url = reverse_lazy('access:Login')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def return_status_stock(self, request, products):
        # request que nos valida primero la compra mediante la deteccion de
        # faltantes en el stock por medio de bases de datos distribuidas
        data = {}
        try:
            validate_transaction = True
            with transaction.atomic():
                for product in products:
                    product_sale = Product.objects.get(id=int(product['id']))
                    ammount_product_size = int(product['amount'])
                    size_sale = Size.objects.get(size_product=product['size'])
                    new_stock = Stock.objects.using('stock_product').get(product=product_sale)
                    new_stocks_size = StockProductSize.objects.using(
                        'stock_product').get(stock=new_stock, size=size_sale)
                    new_stocks_size.amount = new_stocks_size.amount - ammount_product_size
                    new_stocks_size.save(using='stock_product')
                    new_stock.amount = new_stock.amount - ammount_product_size
                    new_stock.save(using='stock_product')
                    if new_stocks_size.amount < 0:
                        validate_transaction = False
                        break
                transaction.set_rollback(True, using='stock_product')
                if validate_transaction == False:
                    data['error'] = 'Stock insuficiente en alguno de tus productos'
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def do_the_purchase(self, request):
        # petición post que realiza con una transacción atómica
        # la venta al sistema
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            products = json.loads(request.POST['products'])
            sale = Sale()
            sale.user = self.request.user
            sale.subtotal = float(request.POST['subtotal'])
            sale.total = float(request.POST['total'])
            direction = DirectionUser.objects.get(id = int(request.POST['direction_user']))
            sale.direction = direction
            sale.save()
            if status_replication:
                sale.save(using='mirror_database')
            sale = Sale.objects.all().latest('id')
            # recorrido de los productos solicitados para su procesamiento
            for product in products:
                detail_sale = DetailSale()
                detail_sale.sale = sale
                product_sale = Product.objects.get(id=int(product['id']))
                detail_sale.product = product_sale
                detail_sale.ammount = int(product['amount'])
                detail_sale.color = product['color']
                size_sale = Size.objects.get(size_product=product['size'])
                detail_sale.size = size_sale
                detail_sale.price = float(product['price']) / detail_sale.ammount
                detail_sale.subtotal = float(product['price'])
                detail_sale.save()
                if status_replication:
                    detail_sale.save(using='mirror_database')
                new_stock = Stock.objects.get(product=product_sale)
                new_stocks_size = StockProductSize.objects.get(stock=new_stock, size=size_sale)
                new_stocks_size.amount = new_stocks_size.amount - detail_sale.ammount
                new_stocks_size.save()
                new_stocks_size.save(using='stock_product')
                if status_replication:
                    new_stocks_size.save(using='mirror_database')
                new_stock.amount = new_stock.amount - detail_sale.ammount
                new_stock.save()
                new_stock.save(using='stock_product')
                if status_replication:
                    new_stock.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # función que valida la cantidad de productos en la tienda
    def validate_update_stock_product(self, request):
        data = {}
        product_id = int(request.POST['product'])
        stock = Stock.objects.get(product=product_id)
        stock_by_size = StockProductSize.objects.filter(stock=stock)
        for st_size in stock_by_size:
            if st_size.size.size_product == request.POST['size']:
                if st_size.amount - int(request.POST['ammount']) > 0:
                    data['success'] = ''
                else:
                    data['error'] = 'No hay suficiente stock'
        return data
    
    # funcion que procesa el json array hacia un nombre del producto
    def __obtain_name_product(self, request):
        raw_products = json.loads(request.POST['products'])
        products = []
        for product in raw_products:
            products.append({'name ' : Product.objects.get(id = int(product['id'])).name})
        return products
    
    # función que procesa el pago con stripe
    def process_data_payment(self, request):
        data = {}
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            DOMAIN_PAGE = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price_data': {
                            'currency' : 'MXN',
                            'unit_amount' : int(float(request.POST['total'])*100),
                            'product_data': {
                                'name' : 'Pago de productos'
                            }
    
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url= DOMAIN_PAGE + reverse_lazy('shop:success'),
                cancel_url= DOMAIN_PAGE + reverse_lazy('shop:cancel'),
            )
            data['id'] = checkout_session.id
        except Exception as e:
            data['error'] = str(e)
        print(data)
        return data

    # sobrescritura del método post para la obtención y guardado de datos
    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        match request.POST['action']:
            # caso de obtención de los colores del producto
            case 'obtain':
                id_prod = int(request.POST['data'])
                product_return = Product.objects.get(id=id_prod)
                data['color1'] = product_return.primary_color
                data['color2'] = product_return.secondary_color
                data['color3'] = product_return.last_color
            # caso donde se valida la edición del producto (cantidad)
            case 'validate':
                data = self.validate_update_stock_product(request)
            # caso donde retorna el nombre del producto y su imagen
            case 'image':
                id_prod = int(request.POST['data'])
                product_return = Product.objects.get(id=id_prod)
                data['image'] = product_return.get_image()
                data['name'] = product_return.name
            # caso donde se prevalida la cantidad total de productos a comprar
            case 'validate_buy':
                products = json.loads(request.POST['products'])
                if len(products) > 0:
                    data = self.return_status_stock(request, products)
                else:
                    data['error'] = 'No hay productos por comprar'
            # caso donde se efectua la compra
            case 'buy':
                with transaction.atomic():
                    data = self.do_the_purchase(request)
                    if 'error' in data:
                        rollback_data(1)
            case 'checkout':
                data = self.process_data_payment(request)
        # retorno de la información como JSON al front-end
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        context['color'] = self.get_number_color()
        context['directions'] = DirectionUser.objects.filter(
            user=self.request.user)
        context['public_stripe'] = STRIPE_PUBLIC_KEY
        return context
