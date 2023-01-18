from django.views.generic.base import TemplateView


class ErrorPageView(TemplateView):
    template_name = 'warning_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Error del sistema'
        return context