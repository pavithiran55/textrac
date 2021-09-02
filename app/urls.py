from django.urls import path
from app import views
from .views import index

urlpatterns = [
    path('', index, name='index')
]