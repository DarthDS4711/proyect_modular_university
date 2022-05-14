import json
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def return_status_stock(self, request):
        # request que nos valida primero la compra mediante la deteccion de
        # faltantes en el stock por medio de bases de datos distribuidas
        data = {}
        try:
            products = json.loads(request.POST['products'])
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
            products = json.loads(request.POST['products'])
            with transaction.atomic():
                sale = Sale()
                sale.user = self.request.user
                sale.subtotal = float(request.POST['subtotal'])
                sale.total = float(request.POST['total'])
                sale.save()
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
                    new_stock = Stock.objects.get(product=product_sale)
                    new_stocks_size = StockProductSize.objects.get(stock=new_stock, size=size_sale)
                    new_stocks_size.amount = new_stocks_size.amount - detail_sale.ammount
                    new_stocks_size.save()
                    new_stocks_size.save(using='stock_product')
                    new_stock.amount = new_stock.amount - detail_sale.ammount
                    new_stock.save()
                    new_stock.save(using='stock_product')
        except Exception as e:
            data['error'] = str(e)
        return data

    # sobrescritura del método post para la obtención y guardado de datos

    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        # caso de obtención de los colores de un producto en particular
        if request.POST['action'] == 'obtain':
            id_prod = int(request.POST['data'])
            product_return = Product.objects.get(id=id_prod)
            data['color1'] = product_return.primary_color
            data['color2'] = product_return.secondary_color
            data['color3'] = product_return.last_color
        elif request.POST['action'] == 'validate':
            product_id = int(request.POST['product'])
            stock = Stock.objects.get(product=product_id)
            stock_by_size = StockProductSize.objects.filter(stock=stock)
            for st_size in stock_by_size:
                if st_size.size.size_product == request.POST['size']:
                    if st_size.amount - int(request.POST['ammount']) > 0:
                        data['success'] = ''
                    else:
                        data['error'] = 'No hay suficiente stock'
        # caso de obtención de la dirección de la imagen y el nombre de un producto
        elif request.POST['action'] == 'image':
            id_prod = int(request.POST['data'])
            product_return = Product.objects.get(id=id_prod)
            data['image'] = product_return.get_image()
            data['name'] = product_return.name
        elif request.POST['action'] == 'validate_buy':
            data = self.return_status_stock(request)
        elif request.POST['action'] == 'buy':
            data = self.do_the_purchase(request)

        # retorno de la información como JSON al front-end
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        context['color'] = self.get_number_color()
        context['directions'] = DirectionUser.objects.filter(
            user=self.request.user)
        return context
