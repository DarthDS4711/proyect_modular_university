from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin


class DashboardAdminView(LoginRequiredMixin, ObtainColorMixin,TemplateView):
    template_name = 'dashboardAdmin.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['status'] = reverse_lazy('status_send:list')
        context['supplier'] = reverse_lazy('supplier_app:list_supplier')
        context['products'] = reverse_lazy('product:list_product')
        context['stock'] = reverse_lazy('stock:list_stock')
        context['store'] = reverse_lazy('shop:main-shop')
        context['color'] = self.get_number_color()
        return context
