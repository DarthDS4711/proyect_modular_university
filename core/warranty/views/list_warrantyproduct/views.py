from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from core.warranty.models import WarrantyProduct



class ListWarrantyProductView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = WarrantyProduct
    paginate_by = 10
    template_name = 'listWarrantyProducts.html'
    login_url = reverse_lazy('access:Login')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de garantías"
        context["create"] = reverse_lazy('warranty:register_incidence')
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context