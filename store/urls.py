from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='pizza-home'),
    path('pizza_cart/', views.cart, name='pizza-cart'),
    path('pizza_contacts/', views.contacts, name='pizza-contacts'),
    path('pizza_about/', views.about, name='pizza-about'),
    path('pizza_menu/', views.menu, name='pizza-menu'),
    #path('cart_add/<int:id>/', views.cart_add, name='cart-add'),
    #path('cart_remove/<int:id>/', views.cart_remove, name='cart-remove')
    path('add_to_cart/<pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<pk>/', views.remove_from_cart, name='remove-from-cart')

]
