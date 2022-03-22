from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class DashboardAdminView(TemplateView):
    template_name = 'dashboardAdmin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['status'] = reverse_lazy('status_send:list')
        context['supplier'] = reverse_lazy('supplier_app:list_supplier')
        context['products'] = reverse_lazy('product:list_product')
        return context
