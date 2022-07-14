from django.http import JsonResponse, QueryDict
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from config.stripe.secret_keys_payment import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.sale.models import Sale


class ListInvoiceView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Sale
    paginate_by = 10
    template_name = 'list_invoices.html'
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
            queryset = Sale.objects.filter(
                user=self.request.user, date_sale__range=(initial_date, final_date))
        else:
            queryset = Sale.objects.filter(user=self.request.user)
        return queryset
    
    def process_data_payment(self, request):
        data = {}
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            DOMAIN_PAGE = "http://127.0.0.1:8000"
            sale_to_pay = Sale.objects.get(id = request.POST['id_product'], user=self.request.user, is_completed=False)
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                customer_email = self.request.user.email,
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price_data': {
                            'currency' : 'MXN',
                            'unit_amount' : int(sale_to_pay.total*100),
                            'product_data': {
                                'name' : f'Pago de productos con atraso usuario: {self.request.user.username}'
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url= DOMAIN_PAGE + reverse_lazy('shop:success'),
                cancel_url= DOMAIN_PAGE + reverse_lazy('shop:cancel'),
            )
            data['id'] = checkout_session.id
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def post(self, request, *args, **kwargs):
        data = {}
        data = self.process_data_payment(request)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial_date, final_date = self.__obtain_range_date()
        context["title"] = "Listado de facturas"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        context['initial_date'] = initial_date
        context['final_date'] = final_date
        context['public_stripe'] = STRIPE_PUBLIC_KEY
        return context
