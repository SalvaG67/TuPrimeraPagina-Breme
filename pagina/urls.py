"""
URL configuration for pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from herreria import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth.views import LogoutView
app_name = 'herreria'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('pedidos/list/', views.pedidos_list, name='listar_pedidos'),
    path('pedidos/update/<int:pk>', views.pedido_update, name='pedido_update'),
    path('pedidos/delete/<int:pk>', views.pedido_delete, name='pedido_delete'),
    path('logout/', LogoutView.as_view(template_name='herreria/logout.html'), name='logout'),
]
urlpatterns += [
    path('productos/list/', views.Productolistview.as_view(), name='listar_productos'),
    path('productos/create/', views.productocreateview.as_view(), name='producto_create'),
    path('productos/update/<int:pk>', views.productoupdateview.as_view(), name='producto_update'),
    path('productos/delete/<int:pk>/', views.productodeleteview.as_view(), name='producto_delete'),
    path('login/', views.miloginview.as_view(), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)