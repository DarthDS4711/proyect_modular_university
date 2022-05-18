from datetime import datetime, timedelta
from django.db import models
from django.forms import model_to_dict
from core.user.models import User
from core.product.models import Product, Size
from core.warranty.models import WarrantyProduct


# table for the sale in the app
class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='user_id', on_delete=models.PROTECT)
    date_sale = models.DateField(default=datetime.now, verbose_name='date_sale')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='subtotal')
    iva = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='iva', default=0.16)
    total = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='iva')


    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = 'Sales'
        ordering = ['id']
        db_table = 'sale'
    
    def get_number_elements(self):
        number_elements_sale = 0
        detail_sales = DetailSale.objects.filter(sale = self)
        for detail_sale in detail_sales:
            number_elements_sale += detail_sale.ammount
        return number_elements_sale
    
    def toJSON(self):
        item = {}
        item['id'] = self.id
        item['user'] = self.user.first_name
        item['date_sale'] = self.date_sale.strftime('%Y-%m-%d')
        item['subtotal'] = format(self.subtotal, ".2f")
        item['iva'] = format(self.iva, ".2f")
        item['total'] = format(self.total, ".2f")
        return item
        

# table for the detail of the sale
class DetailSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    sale = models.ForeignKey(Sale, verbose_name='sale_id', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='product_id', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='price')
    ammount = models.IntegerField(default=0, verbose_name='ammount')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='subtotal')
    color = models.CharField(max_length=8, default='')
    size = models.ForeignKey(Size, verbose_name='size_id', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "DetailSale"
        verbose_name_plural = 'DetailSales'
        ordering = ['id']
        db_table = 'detail_sale'
    
    def get_max_warranty_date(self):
        product_sale = self.product
        date_buy = self.sale.date_sale
        warranty_product = WarrantyProduct.objects.get(product = product_sale).warranty
        months_covered = float(warranty_product.months_coverred)
        date_new = date_buy + timedelta(weeks=(4 * months_covered))
        return date_new
    
    def get_status_warranty(self):
        product_sale = self.product
        date_buy = self.sale.date_sale
        warranty_product = WarrantyProduct.objects.get(product = product_sale).warranty
        months_covered = float(warranty_product.months_coverred)
        date_new = date_buy + timedelta(weeks=(4 * months_covered))
        status = 'Valida' if (date_new - date_buy).days > 0 else 'Caducada'
        return status
        
