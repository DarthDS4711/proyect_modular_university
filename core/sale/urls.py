from django.urls import path

from core.sale.views.list_invoice.views import ListInvoiceView


app_name = 'sale'
urlpatterns = [
    # ruta para listar las facturas del usuario actual
    path('list-invoices/', ListInvoiceView.as_view(), name='list_invoices')
]