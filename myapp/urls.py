from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hero/', views.hero, name='hero'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),

    path('blog-details/', views.blog_details, name='blog_details'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('service-details/', views.service_details, name='service_details'),


]