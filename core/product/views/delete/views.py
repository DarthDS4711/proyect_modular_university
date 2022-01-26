from django.views.generic.base import TemplateView


class DeleteProductView(TemplateView):
    template_name = 'deleteProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar producto"
        context["image"] = "img/delete-product.png"
        return context