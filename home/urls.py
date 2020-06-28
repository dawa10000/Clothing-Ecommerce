from .views import HomeView,CheckoutView,ItemDetailView
from django.urls import path
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),



]