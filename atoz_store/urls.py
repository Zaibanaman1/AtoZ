from django.urls import path,include
from . import views

urlpatterns = [

path('',views.store,name="store"),
path('cart/',views.cart,name="cart"),
path('checkout/',views.checkout,name="checkout"),
path('',views.user,name="user"),
path('updateItem/',views.updateItem,name="updateItem"),
path('processorder/',views.processOrder,name="processorder"),
path('profile/',views.profile,name="profile"),
path('search',views.search,name="search")
]
