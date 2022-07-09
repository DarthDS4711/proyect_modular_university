from datetime import datetime
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.purchase.models import Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from core.sale.models import Sale
from django.db.models import Sum

# vista que nos permitirá comparar nuestros gastos y nuestras ventas
class CompareSalesPurchasesView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = "compare_sales_purchases.html"
    login_url: reverse_lazy("access:Login")
    group_permisson = 'Administrator'

    # método que nos regresa el nombre del mes actual
    def get_name_month(self):
        date_month = datetime.now()
        date_month = date_month.month
        match date_month:
            case 1:
                return "Enero"
            case 2:
                return "Febrero"
            case 3:
                return "Marzo"
            case 4:
                return "Abril"
            case 5:
                return "Mayo"
            case 6:
                return "Junio"
            case 7:
                return "Julio"
            case 8:
                return "Agosto"
            case 9:
                return "Septiembre"
            case 10:
                return "Octubre"
            case 11:
                return "Noviembre"
            case 12:
                return "Diciembre"
    
    # método que nos devuelve la cantidad (total vendido) del mes  y el año actual
    def get_money_related_sales(self):
        date_month = datetime.now().month
        date_year = datetime.now().year
        sales_month = Sale.objects.filter(
            date_sale__year = date_year, date_sale__month = date_month).aggregate(Sum('total'))
        return sales_month['total__sum'] if sales_month['total__sum'] != None else 0.0
    
    # método que nos devuelve la cantidad (total comprado) del mes y año actual
    def get_money_related_purchases(self):
        date_month = datetime.now().month
        date_year = datetime.now().year
        purchases_month = Purchase.objects.filter(
            date_purchase__year = date_year, date_purchase__month = date_month).aggregate(Sum('total'))
        return purchases_month['total__sum'] if purchases_month['total__sum'] != None else 0.0


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sale_month = self.get_money_related_sales()
        total_purchase_month = self.get_money_related_purchases()
        is_bigger_than = True if total_sale_month > total_purchase_month else False
        context['title'] = "Gastos vs Ingresos"
        context['month'] = self.get_name_month()
        context['color'] = self.get_number_color()
        context['sales'] = total_sale_month
        context['purchases'] = total_purchase_month
        context['is_bigger_than'] = is_bigger_than
        return context