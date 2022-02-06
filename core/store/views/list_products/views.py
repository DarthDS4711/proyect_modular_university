from django.views.generic.base import TemplateView


class ListProductsShopView(TemplateView):
    template_name = 'listProductsShop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["title"] = "Categoría Accesorios"
        context["image"] = "img/dress.png"
        context["image1"] = "img/cap.png"
        context["image2"] = "img/pants.png"
        context["image3"] = "img/tshirt.png"
        return context