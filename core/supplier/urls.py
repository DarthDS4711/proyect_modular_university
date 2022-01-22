from django.urls import path

from core.supplier.views.register.views import RegisterSupplierView

app_name = "supplier_app"
urlpatterns = [
    path('register/', RegisterSupplierView.as_view(), name="register_supplier")
]
