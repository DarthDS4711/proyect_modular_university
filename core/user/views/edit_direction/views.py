from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.user.forms.form import DirectionUserForm
from core.user.models import DirectionUser
from django.db import transaction


class UpdateUserDirectionView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = 'direction_notebook/edit_direction.html'
    login_url = reverse_lazy('access:Login')
    model = DirectionUser
    success_url = reverse_lazy('user:list_directions')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def save_direction_user(self, request):
        data = {}
        try:
            name = request.POST['name']
            street = request.POST['street']
            postal_code = int(request.POST['postal_code'])
            exterior_number = request.POST['exterior_number']
            interior_number = request.POST['interior_number']
            is_active = True if request.POST['is_active'] == 'on' else False
            id_direction = self.object.id
            direction_user = DirectionUser.objects.get(id=id_direction)
            # actualización de la instancia de las dirección del usuario
            direction_user.name = name
            direction_user.street = street
            direction_user.postal_code = postal_code
            direction_user.exterior_number = exterior_number
            direction_user.interior_number = interior_number
            direction_user.is_active = is_active
            direction_user.save()
            if is_actual_state_autoreplication():
                direction_user.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data


    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.save_direction_user(request)
            if 'error' in data:
                rollback_data(3)
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(DirectionUserForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar dirección"
        context['action'] = 'update' 
        context['btn'] = 'Actualizar dirección'
        context['color'] = self.get_number_color()
        return context