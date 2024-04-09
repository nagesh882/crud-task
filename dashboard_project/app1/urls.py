from django.urls import path
from app1 import views 


urlpatterns = [
    path("", views.login, name='login'),
    path("sign-up-page/", views.sign_up, name='signup'),
    path("otp_verify/", views.otp_verify, name='otp_verify'),
    path("logout/", views.logout_page, name='logout'),
]
        