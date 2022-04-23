from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='macrames'),
    path('<product_id>', views.product_detail, name='macrame-detail'),
]