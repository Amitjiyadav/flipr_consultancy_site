from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

    # custom admin panel
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/projects/', views.admin_projects, name='admin_projects'),
    path('dashboard/clients/', views.admin_clients, name='admin_clients'),
    path('dashboard/contacts/', views.admin_contacts, name='admin_contacts'),
    path('dashboard/subscribers/', views.admin_subscribers, name='admin_subscribers'),
]
