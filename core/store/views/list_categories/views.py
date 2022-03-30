from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Category


class ListCategoryShopView(ListView):
    model = Category
    paginate_by = 4
    template_name = 'listCategoriesShop.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categorias"
        return context
