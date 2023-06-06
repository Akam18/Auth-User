from django.contrib import admin
from django.urls import path, include
from .views import IndexView, AddProductView, ProductView, IndexView, CategoryView, \
LogoutUserView, SingUpUserView, SignInUserView

urlpatterns = [
    path('', IndexView),
    path('product/', ProductView),
    path('add/', AddProductView),
    path('category/', CategoryView),
    path("signup/", SingUpUserView),
    path('signin/', SignInUserView),
    path("logout/", LogoutUserView),
]
