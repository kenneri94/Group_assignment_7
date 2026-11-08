from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),

    path('blog_details', views.blog_details, name='blog-details'),
    path('porfolio_details/', views.portfolio_details, name='portfolio-details'),
    path('services_details/', views.service_details, name='services-details'),


]