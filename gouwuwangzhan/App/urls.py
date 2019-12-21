from django.contrib import admin
from django.urls import path

from App import views

app_name = 'App'
urlpatterns = [
    path('', views.index, name='index'),
    path('market/', views.show_market, name='show_market'),
    path('mine/', views.show_mine, name='show_mine'),
    path('login/', views.show_login, name='show_login'),
    path('register/', views.user_register, name='user_register'),
    path('checkname/', views.check_username, name='check_username'),
    path('active/', views.user_active, name='user_active'),
    path('logout/',views.user_logout,name='user_logout'),
    path('cart/',views.show_cart,name='show_cart'),
    path('addcart/',views.add_cart,name='add_cart'),
    path('subcart/', views.sub_cart, name='sub_cart'),
    path('changecartstate/',views.change_cart_state,name='change_cart_state'),
    path('subshopping/',views.sub_shopping,name='sub_shopping'),
    path('addshopping/', views.add_shopping, name='add_shopping'),
    path('successcart/', views.success_cart, name='success_cart'),

]
