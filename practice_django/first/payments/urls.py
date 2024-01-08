
from django.urls import path
from . import views 
urlpatterns = [
    path('bk/', views.bk),
    path('rk/', views.rk),
]