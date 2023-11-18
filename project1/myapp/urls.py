from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name='welcome'),
    path("aboutus/", views.aboutus, name='aboutus'),
    path("contactus/", views.contactus, name='contactus'),
    path("generate/", views.generate, name='generate'),
]