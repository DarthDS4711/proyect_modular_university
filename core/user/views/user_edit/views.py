from django.views.generic.base import TemplateView


class EditUserView(TemplateView):
    template_name = 'user_edit/page_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar perfil'
        context['btn_action'] = 'Editar'
        return context