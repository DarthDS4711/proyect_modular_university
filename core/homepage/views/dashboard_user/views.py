from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from django.contrib.sessions.models import Session


class DashboardUserView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'dashboardUser.html'
    login_url = reverse_lazy('access:Login')

    # función que gestiona el número de sesiones ativas
    def __get_number_sessions(self):
        number_sessions = 0
        session_query = Session.objects.all()
        for session in session_query:
            user_key = session.get_decoded().get('_auth_user_id')
            if self.request.user.pk == int(user_key):
                number_sessions += 1
        return number_sessions


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['color'] = self.get_number_color()
        context['number_sessions'] = self.__get_number_sessions()
        return context