from django.views.generic.base import TemplateView


class DashboardUserView(TemplateView):
    template_name = 'dashboardUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context