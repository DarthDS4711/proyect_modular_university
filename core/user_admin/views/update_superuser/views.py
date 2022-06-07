from shutil import which
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

from core.user.models import User



class UpdateSuperUserView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'updateSuperUser.html'
    model = User
    success_url = reverse_lazy('user_admin:list_super_user')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'
    fields = ('is_superuser',)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # función que nos guarda en las bases de datos el estado actual
    # del usuario
    def update_status_user(self, request):
        data = {}
        try:
            user = User.objects.get(id = self.object.id)
            super_user = True if request.POST['status'] == 'True' else False
            user.is_superuser = super_user
            user.save()
            if is_actual_state_autoreplication():
                user.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.update_status_user(request)
            if 'error' in data:
                rollback_data(3)
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Superusuarios"
        context['action'] = 'update' 
        context['superuser'] = self.object.is_superuser
        context['color'] = self.get_number_color()
        context['list'] = self.success_url
        return context