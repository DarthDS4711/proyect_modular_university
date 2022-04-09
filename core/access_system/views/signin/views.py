from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from core.access_system.forms.form import UserForm
from core.user.models import User



class SignInView(CreateView):
    model = User
    success_url = reverse_lazy('app_views:dashboard_user')
    template_name = 'signin.html'

    def get_form(self):
        return super().get_form(UserForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos
            form = self.get_form()
            # guardado de los datos
            data = form.save()
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
        return context
