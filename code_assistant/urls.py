from django.urls import path
# from .views import Home
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]