from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('product_list',views.list_product,name='list_product'),
    path('product_details/<pk>',views.detail_product,name='detail_product')
    

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
