from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_hello, name='blog_hello'),
]