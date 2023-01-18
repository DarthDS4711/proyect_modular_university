from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.http import JsonResponse
from core.user.models import User


class UserPageFlowView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'usersFlow.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def number_active_users(self):
        number_active = User.objects.filter(is_active = True).count()
        return number_active
    
    def number_inactive_users(self):
        number_inactive = User.objects.filter(is_active = False).count()
        return number_inactive

    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            match request.POST['action']:
                case 'active_users':
                    data['users'] = self.number_active_users()
                case 'inactive_users':
                    data['users'] = self.number_inactive_users()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Flujo de usuarios'
        context['active_users'] = self.number_active_users()
        context['inactive_users'] = self.number_inactive_users()
        context['color'] = self.get_number_color()
        return context
