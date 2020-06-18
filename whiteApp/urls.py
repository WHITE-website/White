from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('order', views.order),
    path('form', views.form),
]
