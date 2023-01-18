from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# mixin que nos valida si tenemos una sesión de superusuario activa
class ValidateSuperUserMixin(object):
    url_redirect = None


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('app_views:homepage')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())