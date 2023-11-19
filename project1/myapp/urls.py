from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome, name='welcome'),
    path("aboutus/", views.aboutus, name='aboutus'),
    path("contactus/", views.contactus, name='contactus'),
    path("generate/", views.generate, name='generate'),
    path("", views.login_view, name='login'),
    path("signup/", views.signup_view, name='signup'),
    path("logout/", views.logout_fun, name='logout'),
]