from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from core.access_system.forms.form import UserForm
from core.user.models import User
from core.classes.obtain_color import ObtainColorMixin
from django.db import transaction



class SignInView(CreateView, ObtainColorMixin):
    model = User
    success_url = reverse_lazy('app_views:homepage')
    template_name = 'signin.html'

    def get_form(self):
        return super().get_form(UserForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos
            with transaction.atomic():
                form = self.get_form()
                # guardado de los datos
                data = form.save()
                if 'error' in data:
                    transaction.set_rollback(True)
                    transaction.set_rollback(True, using = 'mirror_database')
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign In"
        context['cancel'] = reverse_lazy('app_views:homepage')
        context['success'] = self.success_url
        context['action'] = 'register' 
        context['color'] = self.get_number_color()
        context['btn'] = 'Crear'
        return context
