from django.shortcuts import render

# Create your views here.
from django.views.generic import View, ListView, DetailView
from .models import *

class BaseView(View):
    view = {}

class HomeView(BaseView):
    def get(self,request):
        self.view['items'] = Item.objects.all()
        return render(self.request, 'home-page.html', self.view)

class CheckoutView(BaseView):
    def get(self,request):

        return render(request,'checkout-page.html',self.view)

class ProductView(BaseView):
    def get(self,request):

        return render(request,'product-page.html',self.view)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'