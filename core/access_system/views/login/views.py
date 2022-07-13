from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin



class LoginView(EmergencyModeMixin, FormView, ObtainColorMixin):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('app_views:dashboard_user')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        data = {}
        user = authenticate(request, username=username, password=password)
        if user is None:
            data['error'] = 'Usuario o contraseña no válidos'
        else:
            login(request, user)
            data['success'] = self.success_url
        return JsonResponse(data, safe=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Login"
        context['color'] = self.get_number_color()
        return context
    
