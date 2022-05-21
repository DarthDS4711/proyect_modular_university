from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from django.contrib.auth.models import Group
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Category
from core.sale.models import DetailSale, Sale
from django.http import JsonResponse


class DashboardAdminView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin,TemplateView):
    template_name = 'dashboardAdmin.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    @csrf_exempt
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
        sale_num = Sale.objects.filter(date_sale__month = date_time_month).count()
        return sale_num
    
    def get_sales_by_week(self):
        list_sale_days = []
        counter = 6
        while counter >= 0:
            date = (datetime.now() - timedelta(counter)) 
            sales_per_day =  Sale.objects.filter(date_sale = date).count()
            list_sale_days.append(sales_per_day)
            counter -= 1
        return list_sale_days


    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['action'] == 'pie_g':
                data['number_sale'] = self.get_number_sale_per_category()
                data['labels'] = self.get_names_categories()
            elif request.POST['action'] == "bar_month":
                data['sale_month'] = self.get_sales_by_month()
            elif request.POST['action'] == 'bar_week':
                data['sale_week'] = self.get_sales_by_week()
            
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
