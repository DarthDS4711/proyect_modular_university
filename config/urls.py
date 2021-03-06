"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unittest.mock import patch
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # rutas relacionadas a la página principal tales como dashboard
    path('', include('core.homepage.urls')),
    # rutas relacionadas a los accesos del sistema, tales como ingresar, registrar
    path('access/', include('core.access_system.urls')),
    # rutas relacionadas a los proveedores tales como registrarlos, eliminarlos
    path('supplier/', include('core.supplier.urls')),
    # rutas relacionadas a los productos tales como registrar, eliminar, actualizar
    path('product/', include('core.product.urls')),
    # rutas relacionadas a la tienda tales como visualizar producto, comprar producto
    path('shop/', include('core.store.urls')),
    # rutas relacionadas a el estado actual de envio de los productos
    path('send/', include('core.status_send.urls')),
    # rutas relacionadas a las garantías de los productos e incidentes
    path('warranty/', include('core.warranty.urls')),
    # rutas relacionadas a la cantidad de productos disponibles en el sistema
    path('stock/', include('core.stock.urls')),
    # rutas relacionadas con el usuario
    path('user/', include('core.user.urls')),
    # rutas relacionadas al color de la página
    path('color-page/', include('core.colorpage.urls')),
    # rutas relacionadas con la facturación del usuario
    path('sale/', include('core.sale.urls')),
    # rutas relacionadas con la subida de facturas al sistema
    path('purchase/', include('core.purchase.urls')),
    # rutas relacionadas con la replicación automática de los datos
    path('data-application/', include('core.data.urls')),
    # rutas relacionadas a la administración de los usuarios
    path('user-admin/', include('core.user_admin.urls')),
    # rutas relacionadas con la administración de la aplicacion
    path('admin_site/', include('core.admin_site.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
