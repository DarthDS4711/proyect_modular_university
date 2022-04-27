from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from core.mixins.mixins import ValidateSessionGroupMixin
from core.warranty.models import Incidence



class ListIncidencesView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Incidence
    paginate_by = 10
    template_name = 'listIncidences.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de incidencias"
        context["create"] = reverse_lazy('warranty:register_incidence')
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context