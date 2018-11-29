from django.urls import path

from . import views


urlpatterns = [
    path('', views.list_products, name='list'),
    path('v2', views.ProductListView.as_view(), name='list-2'),
    path('buy/<int:pk>/', views.buy_product, name='buy'),
    path('contact/', views.contract_form_action, name='contact'),
]
