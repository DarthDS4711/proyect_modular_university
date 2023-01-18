from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session
from core.mixins.emergency_mixin import EmergencyModeMixin
from django.views.generic.base import View


class LogoutUserView(EmergencyModeMixin, LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('app_views:homepage')
    template_name = 'index.html'

class LogoutAllSessionUserView(EmergencyModeMixin, LoginRequiredMixin, View):
    next_page = reverse_lazy('app_views:homepage')

    def dispatch(self, request, *args, **kwargs):
        session_query = Session.objects.all()
        for session in session_query:
            user_key = session.get_decoded().get('_auth_user_id')
            if self.request.user.pk == int(user_key):
                session.get_decoded()
                session.delete()
        return HttpResponseRedirect(self.next_page)