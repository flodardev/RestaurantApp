from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("register", views.register, name="register"),
    path("login", views.loginPage, name="login",),
    path("logout", views.logoutUser, name="logout"),

    path("menu", views.menu, name="menu"),
    path("sub", views.sub, name="sub"),
    path("pasta", views.pasta, name="pasta"),
    path("salad", views.salad, name="salad"),
    path("dinnerplatter", views.dinnerplatter, name="dinnerplatter"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"),
    path("payment", views.payment_cart, name="payment")
]
