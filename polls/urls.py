from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    #path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]