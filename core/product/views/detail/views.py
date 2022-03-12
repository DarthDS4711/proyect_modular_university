from django.views.generic.detail import DetailView
from core.product.models import Category


class DetailCategoryView(DetailView):
    model = Category
    template_name = "detailCategory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle categoría'
        return context