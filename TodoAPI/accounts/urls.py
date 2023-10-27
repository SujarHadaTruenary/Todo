from django.urls import path, include
from app_name import views

urlpatterns = [
    # register
    path('accounts/register/', views.register.as_view(), name='register'),

    # #users
    path('accounts/user/', views.User.as_view(), name='user'),
    # path ('user/<int:pk>', views.UserView.as_view()),
    #
    # #otp
    path('accounts/otp/', views.OtpView.as_view(), name='otp'),
]
