from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('single-post/', views.single_post, name='single_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
