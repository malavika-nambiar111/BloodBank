from django.urls import path
from blood import views

urlpatterns = [
  
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patient/', views.patient, name='patient'),
    path('donor/', views.donor, name='donor'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
]