from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Comment, Product
from core.stock.models import Stock, StockProductSize
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt

from core.warranty.models import WarrantyProduct, WarrantySale



class DetailProductView(LoginRequiredMixin, ObtainColorMixin , DetailView):
    template_name = "detailProductShop.html"
    model = Product
    login_url = reverse_lazy('access:Login')


    @csrf_exempt    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    # sobrescritura del método post para la obtención y guardado de datos
    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        stock = Stock.objects.get(product = self.object)
        stock_by_size = StockProductSize.objects.filter(stock = stock)
        for st_size in stock_by_size:
            if st_size.size.size_product == request.POST['size']:
                if st_size.amount - int(request.POST['ammount']):
                    data['success'] = ''
                else:
                    data['error'] = 'No hay suficiente stock'
        return JsonResponse(data, safe=False)

    # método que bloquea o habilita el botón de agregar al carrito
    def return_status_stock(self):
        stock = Stock.objects.get(product=self.object.id)
        if stock is not None:
            if stock.amount > 0:
                return True
            else:
                return False
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        context['stock'] = self.return_status_stock()
        context['color'] = self.get_number_color()
        # obtención del comentario de la mejor valoración
        len_comments = Comment.objects.filter(
            product = self.object).order_by('-valoration_user').count()
        if len_comments > 0:
            context['comment'] = Comment.objects.filter(
                product = self.object).order_by('-valoration_user')[0]
        else:
            context['comment'] = "None"
        warranty = WarrantyProduct.objects.filter(product = self.object)
        if warranty.exists():
            context['warranty'] = warranty[0]
        else:
            context['warranty'] = 'None'
        return context