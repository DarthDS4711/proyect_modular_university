from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.views.generic.base import TemplateView



class OptionsPurchaseView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'optionsPurchase.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Opciones de compras"
        context['btn'] = 'Registrar producto'
        context['color'] = self.get_number_color()
        return context