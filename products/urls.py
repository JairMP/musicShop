from django.urls import path
from . import views

urlpatterns = [
    path('<pk>', views.ProductDatailView.as_view(), name='product'),
]