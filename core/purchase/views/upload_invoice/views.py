import json
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product, Size
from core.purchase.models import DetailPurchase, Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# clase para crear los stock
class UpdloadPurchaseView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'uploadInvoice.html'
    model = Purchase
    success_url = reverse_lazy('purchae:options')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'
    fields = ('iva',)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def upload_invoice(self, request):
        data = {}
        products = json.loads(request.POST['products'])
        total_invoice = float(request.POST['total'])
        subtotal_purchase = float(request.POST['subtotal'])
        try:
            with transaction.atomic():
                purchase = Purchase()
                purchase.total = total_invoice
                purchase.subtotal = subtotal_purchase
                purchase.save()
                for product in products:
                    detail_invoice = DetailPurchase()
                    detail_invoice.purchase = purchase
                    product_invoice = Product.objects.get(id = int(product['id']))
                    detail_invoice.product = product_invoice
                    size_product_invoice = Size.objects.get(id = int(product['size']))
                    detail_invoice.size = size_product_invoice
                    detail_invoice.ammount = int(product['ammount'])
                    detail_invoice.color = product['color']
                    detail_invoice.price = float(product['pvp']) / detail_invoice.ammount
                    detail_invoice.subtotal = float(product['pvp'])
                    detail_invoice.save()
        except Exception as e:
            data['error'] = str(e)
        return data



    def post(self, request, *args, **kwargs):
        data = {}
        match request.POST['action']:
            # caso de autocomplete para el select2 el el frontend
            case "autocomplete":
                data = []
                product_data = Product.objects.filter(name__icontains = request.POST['term'])
                for product in product_data:
                    item = product.to_json_faster()
                    item['text'] = f'Producto: {product.name}'
                    data.append(item)
            # caso en el que obtenemos un producto que hayamos seleccionado previamente
            case "get_product":
                product_selected = Product.objects.get(id = int(request.POST['id_product']))
                product_selected = product_selected.to_json()
                data['product'] = product_selected
            # caso en el que devolvemos la imagen de un producto y su nombre
            case "image":
                id_prod = int(request.POST['data'])
                product_return = Product.objects.get(id = id_prod)
                data['image'] = product_return.get_image()
                data['name'] = product_return.name
            # caso de hacer efectiva la subida de la factura
            case "upload_invoice":
                data = self.upload_invoice(request)
            
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Subir una factura"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['color'] = self.get_number_color()
        return context