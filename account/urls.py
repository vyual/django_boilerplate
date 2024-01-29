from django.urls import path

from account import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
