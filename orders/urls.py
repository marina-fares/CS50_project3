from django.urls import path

from . import views

app_name='orders'
urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("menu/", views.menu_view, name="menu"),
]
