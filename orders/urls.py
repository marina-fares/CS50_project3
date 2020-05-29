from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu_view, name="menu"),
    path("save_order/", views.save_order, name="save_order"),
    path("show_order/", views.show_order, name="show_order"),
    path("send_order/", views.send_order, name="send_order"),
]
