from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin


class ListCategoryShopView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Category
    paginate_by = 4
    template_name = 'listCategoriesShop.html'
    login_url = reverse_lazy('access:Login')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categorias"
        context['color'] = self.get_number_color()
        return context
