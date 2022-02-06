from django.urls import path

from core.stock.views.detail_stock.views import DetailStockProduct


app_name = 'stock'

urlpatterns = [
    path('detail/', DetailStockProduct.as_view(), name='detail-stock')
]