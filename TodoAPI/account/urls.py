from django.urls import path, include
from app_name import views

urlpatterns = [
    # register
    path('account/register/', views.register.as_view(), name='register'),

    # #users
    path('account/user/', views.User.as_view(), name='user'),
    # path ('user/<int:pk>', views.UserView.as_view()),
    #
    # #otp
    path('account/otp/', views.OtpView.as_view(), name='otp'),
]
