from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin



class DetailCategoryView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, DetailView):
    model = Category
    template_name = "detailCategory.html"
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle categoría'
        context['color'] = self.get_number_color()
        return context


class DetailProductView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin ,DetailView):
    model = Product
    template_name = 'detailProduct.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle producto'
        context['color'] = self.get_number_color()
        return context