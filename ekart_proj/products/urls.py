from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.product_list, name='product_list'),
    path('product_details', views.product_details, name='product_details')
]
