from django.urls import path
from . import views


urlpatterns = [
path("loginm",views.loginm,name="loginm"),
path("managerdash",views.managerdash,name="managerdash")


]