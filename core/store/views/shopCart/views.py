from itertools import product
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from django.views.decorators.csrf import csrf_exempt

from core.product.models import Product


class ShopCartView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = "shopCart.html"
    login_url = reverse_lazy('access:Login')


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobrescritura del método post para la obtención y guardado de datos
    def post(self, request, *args, **kwargs):
        data = {}
        # caso de obtención de los colores de un producto en particular
        if request.POST['action'] == 'obtain':
            id_prod = int(request.POST['data'])
            product_return = Product.objects.get(id=id_prod)
            data['color1'] = product_return.primary_color
            data['color2'] = product_return.secondary_color
            data['color3'] = product_return.last_color
        # caso de obtención de la dirección de la imagen y el nombre de un producto
        elif request.POST['action'] == 'image':
            id_prod = int(request.POST['data'])
            product_return = Product.objects.get(id=id_prod)
            data['image'] = product_return.get_image()
            data['name'] = product_return.name
        # retorno de la información como JSON al front-end
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        context['color'] = self.get_number_color()
        return context
    