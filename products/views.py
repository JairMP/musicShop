from typing import List
from django.db.models import query
from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import Product
from django.db.models import Q

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ProductDatailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(name__icontains=self.query()) | Q(category__name__icontains=self.query())
        return Product.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.query()
        context['count'] = context['product_list'].count()

        return context
