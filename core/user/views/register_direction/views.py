from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.user.forms.form import DirectionUserForm
from core.user.models import DirectionUser


class RegisterDirectionUser(LoginRequiredMixin, ObtainColorMixin, CreateView):
    template_name = 'direction_notebook/register_direction.html'
    login_url = reverse_lazy('access:Login')
    model = DirectionUser
    success_url = reverse_lazy('user:list_directions')


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos referentes a la dirección del usuario 
            direction = request.POST['direction']
            is_active = True if request.POST['is_active'] == 'on' else False
            direction_user = DirectionUser()
            # creación de la instancia de las dirección del usuario
            direction_user.user = self.request.user
            direction_user.direction = direction
            direction_user.is_active = is_active
            direction_user.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(DirectionUserForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar dirección"
        context['action'] = 'register' 
        context['btn'] = 'Registrar dirección'
        context['color'] = self.get_number_color()
        return context