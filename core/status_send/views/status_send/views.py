from django.views.generic.base import TemplateView


class StatusSendView(TemplateView):
    template_name = "statusSend.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Status envio de productos"
        return context