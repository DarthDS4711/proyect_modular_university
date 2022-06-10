from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.user.models import User


class ListAdminUserView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = User # modelo a usar para la consulta del ListView
    paginate_by = 6 # número de elementos a mostrar por pagina
    template_name = 'listAdminUser.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        elif 'name' in self.request.GET:
            return self.request.GET['name']
        else:
            return ''

    def get_queryset(self):
        return User.objects.all().exclude(id = self.request.user.id
        ).filter(username__icontains = self.return_name())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de usuarios administradores"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        context['name'] = self.return_name()
        context['url'] = reverse_lazy('user_admin:list_admin_user')
        return context

