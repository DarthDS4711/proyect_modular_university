from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.user.models import User
from django.contrib.auth import logout


class EditPasswordLoginView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = 'edit_password/new_password.html'
    login_url = reverse_lazy('access:Login')
    success_url = reverse_lazy('app_views:dashboard_user')
    model = User
    fields = '__all__'
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def get_object(self):
        return self.request.user
    

    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            self.object.set_password(new_password)
            self.object.save()
            logout(request)
        else:
            data['error'] = 'Las contraseñas no coinciden'
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar contraseña"
        context['action'] = 'update' 
        context['btn'] = 'Actualizar contraseña'
        context['color'] = self.get_number_color()
        return context
    