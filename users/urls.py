from django.urls import path
from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from orders import views as view_orders

app_name='users'

urlpatterns = [
    url(r'^$', view_orders.home, name='home'),
    url(r'^login',LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout', LoginView.as_view(template_name='home.html'), name="logout"),
    url(r'^register', views.register, name='register'),
]