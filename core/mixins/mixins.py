from crum import get_current_request
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


class ValidateSessionGroupMixin(object):
    url_redirect = None
    group_permisson = 'Client'


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('app_views:homepage')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if request.user.groups.filter(name = self.group_permisson).exists():
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())