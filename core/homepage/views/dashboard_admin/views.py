from datetime import datetime, timedelta
from platform import libc_ver
from urllib import response
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Category
from core.sale.models import DetailSale, Sale
from django.http import JsonResponse
from core.mixins.emergency_mixin import EmergencyModeMixin
import requests


class DashboardAdminView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin,TemplateView):
    template_name = 'dashboardAdmin.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_number_sale_per_category(self):
        categories = Category.objects.all()
        list_number_sale_per_category = []
        for category in categories:
            sale_number = DetailSale.objects.filter(product__category = category).count()
            list_number_sale_per_category.append(sale_number)
        return list_number_sale_per_category
    
    def get_names_categories(self):
        list_names_categories = []
        categories = Category.objects.all()
        for category in categories:
            list_names_categories.append(category.name)
        return list_names_categories
    
    def get_sales_by_month(self):
        date_time_month = datetime.now().month
        date_time_year = datetime.now().year
        sale_num = Sale.objects.filter(
            date_sale__month = date_time_month, date_sale__year = date_time_year).count()
        return sale_num
    
    def get_sales_by_month_for_ia(self):
        max_month = datetime.now().month - 1
        current_month = 1
        current_year = datetime.now().year
        list_sales_per_month = []
        list_of_month = []
        while current_month <= max_month:
            sale_of_month = Sale.objects.filter(
                date_sale__month = current_month, date_sale__year = current_year).count()
            list_sales_per_month.append(sale_of_month)
            list_of_month.append(current_month)
            current_month += 1
        return list_sales_per_month, list_of_month
    
    def get_sales_by_week(self):
        list_sale_days = []
        counter = 6
        while counter >= 0:
            date = (datetime.now() - timedelta(counter)) 
            sales_per_day =  Sale.objects.filter(date_sale = date).count()
            list_sale_days.append(sales_per_day)
            counter -= 1
        return list_sale_days
    
    # function allows to send to api_ia data for prediction of sale of week
    def __request_prediction_week_from_api(self):
        uri = "http://localhost:8080/sale/prediction/"
        body = {
            "data_x" : [1, 2 ,3 ,4 ,5 , 6, 7],
            "data_y" : self.get_sales_by_week(),
            "data_predict" : 8
        }
        response = requests.get(uri, json = body)
        return response.json()
    
    # function allows to send to api_ia data for prediction of sale of month
    def __request_prediction_month_from_api(self):
        sales_per_month, list_months = self.get_sales_by_month_for_ia()
        uri = "http://localhost:8080/sale/prediction/"
        body = {
            "data_x" : list_months,
            "data_y" : sales_per_month,
            "data_predict" : datetime.now().month
        }
        response = requests.get(uri, json = body)
        return response.json()
    

    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            match request.POST['action']:
                case 'pie_g':
                    data['number_sale'] = self.get_number_sale_per_category()
                    data['labels'] = self.get_names_categories() 
                case 'bar_month':
                    data['sale_month'] = self.get_sales_by_month() 
                case 'bar_week':
                    data['sale_week'] = self.get_sales_by_week()
                case 'prediction_sale_week':
                    data = self.__request_prediction_week_from_api()
                case 'prediction_sale_month':
                    data = self.__request_prediction_month_from_api()
            
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['status'] = reverse_lazy('status_send:list')
        context['supplier'] = reverse_lazy('supplier_app:list_supplier')
        context['products'] = reverse_lazy('product:list_product')
        context['stock'] = reverse_lazy('stock:list_stock')
        context['store'] = reverse_lazy('shop:main-shop')
        context['color'] = self.get_number_color()
        return context
