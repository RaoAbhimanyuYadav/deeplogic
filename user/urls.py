from django.urls import path
from .views import loginUser, logoutUser, registerUser, homepage

urlpatterns = [
    # path("login/", loginUser, name='login'),
    # path("logout/", logoutUser, name='logout'),
    # path("register/", registerUser, name='register'),
    path("", homepage, name='homepage')
]
