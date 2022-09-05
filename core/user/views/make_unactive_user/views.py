from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.user.models import User
from django.contrib.auth import logout
from django.db import transaction


class EditStatusActualUser(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = 'make_unactive_user/make_invalid_user.html'
    login_url = reverse_lazy('access:Login')
    model = User
    fields = '__all__'
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def get_object(self):
        return self.request.user
    
    # función que actualiza el status de nuestro usuario actual
    def make_inactive_user(self, request):
        data = {}
        try:
            make_inactive = True if request.POST['is_active'] == 'False' else False
            if make_inactive:
                self.object.is_active = False
                self.object.save()
                if is_actual_state_autoreplication():
                    self.object.save(using='mirror_database')
                session_query = Session.objects.all()
                for session in session_query:
                    user_key = session.get_decoded().get('_auth_user_id')
                    if self.request.user.pk == int(user_key):
                        session.get_decoded()
                        session.delete() 
        except Exception as e:
            data['error'] = str(e)
        return data
    

    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        with transaction.atomic():
            data = self.make_inactive_user(request)
            if 'error' in data:
                rollback_data(3)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dar de baja la cuenta"
        context['action'] = 'update' 
        context['btn'] = 'Dar de baja'
        context['color'] = self.get_number_color()
        return context
    