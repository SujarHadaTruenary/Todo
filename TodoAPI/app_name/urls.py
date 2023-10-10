from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo',views.TodoView)
router.register('user',views.UserView)
router.register('otp',views.OtpView)


urlpatterns = [
     path('',include(router.urls)),
]