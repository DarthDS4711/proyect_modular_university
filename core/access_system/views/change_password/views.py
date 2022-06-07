from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from core.access_system.forms.form_change_pwd import ChangePasswordForm
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.classes.obtain_color import ObtainColorMixin
from core.user.models import User
from django.db import transaction
import uuid


# vista que cambia la contraseña y el token del usuario
class ChangePasswordUseriew(FormView, ObtainColorMixin):
    template_name = 'change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('app_views:homepage')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobreecsritura del método get para en caso de un link
    # inválido los mande a una página de 404
    def get(self, request, *args, **kwargs):
        user_token = self.kwargs['token']
        if User.objects.filter(token = user_token).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('app_views:404_page'))
    

    # método que actualiza la contraseña y el token del usuario
    def update_password_token_user(self, new_password):
        data = {}
        try:
            with transaction.atomic():
                user = User.objects.get(token = self.kwargs['token'])
                user.set_password(new_password)
                user.token = uuid.uuid4()
                user.save()
                if is_actual_state_autoreplication():
                    user.save(using = 'mirror_database')
                data['success'] = reverse_lazy('access:Login')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # sobreecsritura del método post para 
    def post(self, request, *args, **kwargs):
        data = {}
        new_password = request.POST['id_password']
        confirm_password = request.POST['id_confirmPassword']
        if new_password == confirm_password:
            data = self.update_password_token_user(new_password)
        else:
            data['error'] = 'Las contraseñas no coinciden'
        print(data)
        return JsonResponse(data, safe=True)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Formulario de cambio de contraseña"
        context['color'] = self.get_number_color()
        return context
    
