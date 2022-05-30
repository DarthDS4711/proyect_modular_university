from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.user.forms.form import DirectionUserForm
from core.user.models import DirectionUser


class UpdateUserDirectionView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = 'direction_notebook/edit_direction.html'
    login_url = reverse_lazy('access:Login')
    model = DirectionUser
    success_url = reverse_lazy('user:list_directions')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos referentes a la dirección del usuario 
            direction = request.POST['direction']
            is_active = True if request.POST['is_active'] == 'on' else False
            id_direction = self.object.id
            direction_user = DirectionUser.objects.get(id=id_direction)
            # actualización de la instancia de las dirección del usuario
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
        context["title"] = "Actualizar dirección"
        context['action'] = 'update' 
        context['btn'] = 'Actualizar dirección'
        context['color'] = self.get_number_color()
        return context