from django.urls import path
from . import views

app_name= 'products'

urlpatterns = [
    path('search/', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDatailView.as_view(), name='product')
]