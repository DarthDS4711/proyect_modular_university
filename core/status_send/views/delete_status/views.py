from django.views.generic.base import TemplateView


class DeleteStatusSendView(TemplateView):
    template_name = 'deleteStatusSend.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Estado de Envio"
        context["image"] = "img/delete_status_send.png"
        return context