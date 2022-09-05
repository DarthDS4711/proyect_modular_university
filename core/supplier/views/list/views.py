from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product
from core.supplier.models import Supplier
from django.db.models import Q


class ListSupplierView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Supplier # modelo a usar para la consulta del ListView
    paginate_by = 10 # número de elementos a mostrar por pagina
    template_name = 'listSupplier.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        elif 'name' in self.request.GET:
            return self.request.GET['name']
        else:
            return ''
    
    def return_status(self):
        if 'status' in self.kwargs.keys():
            return self.kwargs['status']
        elif 'status' in self.request.GET:
            return self.request.GET['status']
        else:
            return ''
    
    def return_queryset_with_filter(self, suppliers, status):
        match status:
            case '':
                return suppliers
            case '1':
                return suppliers
            case '2':
                return suppliers.filter(is_active=True)
            case '3':
                return suppliers.filter(is_active=False)
    
    def get_queryset(self):
        name = self.return_name()
        status = self.return_status()
        if name != '':
            suppliers = Supplier.objects.filter(Q(first_names__icontains=name) | Q(last_names__icontains=name))
            return self.return_queryset_with_filter(suppliers, status)
        else:
            suppliers = Supplier.objects.all()
            return self.return_queryset_with_filter(suppliers, status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de proveedores"
        context["create"] = reverse_lazy('supplier_app:register_supplier')
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        context['url'] = reverse_lazy('supplier_app:list_supplier')
        context['name'] = self.return_name()
        context['status'] = self.return_status()
        return context


class ListAllProductSupplierView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 2
    template_name = 'listAllProductsOfSupplier.html'
    login_url = reverse_lazy('access:Login')

    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        elif 'name' in self.request.GET:
            return self.request.GET['name']
        else:
            return ''
    
    def return_id_supplier(self):
        if 'id_supplier' in self.kwargs.keys():
            return int(self.kwargs['id_supplier'])
        elif 'id_supplier' in self.request.GET:
            return int(self.request.GET['id_supplier'])

    def get_queryset(self):
        name_product = self.return_name()
        id_supplier = self.return_id_supplier()
        print(id_supplier)
        if name_product != '':
            return Product.objects.filter(supplier_id=id_supplier, name__icontains=name_product)
        else:
            return Product.objects.filter(supplier_id=id_supplier)
    

    def get_context_data(self, **kwargs):
        name = Supplier.objects.get(id=self.return_id_supplier())
        context = super().get_context_data(**kwargs)
        context['title'] = f'Productos del proveedor: {name.get_name()}'
        context['color'] = self.get_number_color()
        context['url'] = reverse_lazy('supplier_app:list_only_products')
        context['name'] = self.return_name()
        context['id_supplier'] = self.return_id_supplier()
        return context
    

