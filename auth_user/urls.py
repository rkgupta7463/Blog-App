from django.urls import path
from .views import loginUser, logOutUser, signupUser

urlpatterns = [
    path("signup/",signupUser , name="signup"),
    path("login/",loginUser , name="login"),
    path("logout/",logOutUser , name="logout"),
]
