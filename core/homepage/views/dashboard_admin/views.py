from django.views.generic.base import TemplateView


class DashboardAdminView(TemplateView):
    template_name = 'dashboardAdmin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context
