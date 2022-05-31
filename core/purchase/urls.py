from django.urls import path
from core.purchase.views.compare_sales_purchases.views import CompareSalesPurchasesView
from core.purchase.views.list_invoices_system.views import ListInvoiceSystemView

from core.purchase.views.options_purchase.views import OptionsPurchaseView
from core.purchase.views.upload_invoice.views import UpdloadPurchaseView


app_name = "purchase"
urlpatterns = [
    # ruta general para mostrar la pantalla de subida de las compras
    path("options/", OptionsPurchaseView.as_view(), name="options"),
    #ruta para subir las facturas
    path("upload-invoice/", UpdloadPurchaseView.as_view(), name="upload"),
    # ruta para listar todas las facturas del sistema
    path("list-invoices/", ListInvoiceSystemView.as_view(), name="list_invoices"),
    # ruta para comparar los gastos e ingresos del mes actual
    path("comparation/", CompareSalesPurchasesView.as_view(), name="comparation")
]