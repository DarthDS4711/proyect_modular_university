import os
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from core.classes.obtain_color import ObtainColorMixin
from core.sale.models import DetailSale, Sale
from django.template.loader import get_template
from weasyprint import HTML, CSS


class RenderDetailInvoiceView(LoginRequiredMixin, ObtainColorMixin, View):
    login_url = reverse_lazy('access:Login')
    

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('invoice.html')
            invoice = Sale.objects.get(id = int(self.kwargs['pk']))
            detail_invoice = DetailSale.objects.filter(sale = invoice)
            context = {
                'details' : detail_invoice,
                'object' : invoice,
                'number_elements' : invoice.get_number_elements(),
                'iva' : '16%'
            }
            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/libs/bootstrap-4.4.1-dist/css/bootstrap.min.css')
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('sale:list_invoices'))