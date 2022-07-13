from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from django.views.generic.list import ListView
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.user.models import DirectionUser


class ListDirectionUserView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, ListView):
    template_name = 'direction_notebook/list_direction_notebook.html'
    login_url = reverse_lazy('access:Login')
    model = DirectionUser
    paginate_by = 20

    def get_queryset(self):
        query_set = DirectionUser.objects.filter(user=self.request.user.id)
        return query_set


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Libreta de direcciones"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context