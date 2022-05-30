from django.urls import path

from core.purchase.views.options_purchase.views import OptionsPurchaseView
from core.purchase.views.upload_invoice.views import UpdloadPurchaseView


app_name = "purchase"
urlpatterns = [
    # ruta general para mostrar la pantalla de subida de las compras
    path("options/", OptionsPurchaseView.as_view(), name="options"),
    #ruta para subir las facturas
    path("upload-invoice/", UpdloadPurchaseView.as_view(), name="upload")
]