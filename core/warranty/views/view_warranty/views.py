from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.stock.models import Stock
from django.contrib.auth.mixins import LoginRequiredMixin

from core.warranty.models import WarrantySale



class DetailWarrantyView(LoginRequiredMixin, ObtainColorMixin , DetailView):
    template_name = "detailWarranty.html"
    model = WarrantySale
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        context['color'] = self.get_number_color()
        return context