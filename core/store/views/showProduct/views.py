from django.views.generic.detail import DetailView
from core.product.models import Product



class DetailProductView(DetailView):
    template_name = "detailProductShop.html"
    model = Product

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context