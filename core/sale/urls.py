from django.urls import path
from core.sale.views.detail_invoice.views import DetailInvoiceView

from core.sale.views.list_invoice.views import ListInvoiceView
from core.sale.views.render_pdf_invoice.views import RenderDetailInvoiceView


app_name = 'sale'
urlpatterns = [
    # ruta para listar las facturas del usuario actual
    path('list-invoices/', ListInvoiceView.as_view(), name='list_invoices'),
    # ruta para obtener los detalles de la factura actual
    path('detail-invoice/<pk>', DetailInvoiceView.as_view(), name='detail_invoice'),
    # ruta para generar el pdf de la factura
    path('render-pdf-invoice/<pk>', RenderDetailInvoiceView.as_view(), name='render_pdf')
]