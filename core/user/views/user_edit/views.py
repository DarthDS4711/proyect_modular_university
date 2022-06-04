from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from core.app_functions.rollback_data import rollback_data
from core.user.forms.form_user import UserEditForm
from core.user.models import User
from core.classes.obtain_color import ObtainColorMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction



class UpdateUserView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    model = User
    success_url = reverse_lazy('app_views:homepage')
    template_name = 'signin.html'
    login_url = reverse_lazy('access:Login')

    def get_form(self):
        return super().get_form(UserEditForm)
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            # obtención de los datos
            form = self.get_form()
            # guardado de los datos
            data = form.save()
            if 'error' in data:
                rollback_data(3)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar perfil"
        context['cancel'] = reverse_lazy('app_views:homepage')
        context['success'] = self.success_url
        context['action'] = 'update' 
        context['color'] = self.get_number_color()
        context['btn'] = 'Actualizar'
        return context
