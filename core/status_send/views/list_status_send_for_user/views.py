from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.status_send.models import StatusSendSale


class ListStatusUserSendView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = StatusSendSale
    paginate_by = 10
    template_name = 'list_status_send_user.html'
    login_url = reverse_lazy('access:Login')

    def __obtain_range_date(self):
        initial_date = self.request.GET['initial_date'] if 'initial_date' in self.request.GET.keys(
        ) else ''
        final_date = self.request.GET['final_date'] if 'final_date' in self.request.GET.keys(
        ) else ''
        return initial_date, final_date

    def get_queryset(self):
        queryset = None
        initial_date, final_date = self.__obtain_range_date()
        if initial_date != '' and final_date != '':
            queryset = StatusSendSale.objects.filter(
                sale__user = self.request.user, date_arrival__range=[initial_date, final_date])
        else:
            queryset = StatusSendSale.objects.filter(sale__user = self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial_date, final_date = self.__obtain_range_date()
        context['title'] = 'Estado de envio de las facturas'
        context['color'] = self.get_number_color()
        context['initial_date'] = initial_date
        context['final_date'] = final_date
        return context