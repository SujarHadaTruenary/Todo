from django.urls import path, include
from app_name import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('todo',views.TodoView)
# router.register('user',views.UserView)
# router.register('otp',views.OtpView)

# router.register_action(
#     'todo',
#     'create',
#     views.TodoView.as_view({'post': 'create'}),
#     name='todo-create',
# )



urlpatterns = [
     #todos
     path('', views.TodoView.as_view(), name='todo'),
     path('todo/<int:pk>/', views.TodoView.as_view(), name='todo-detail'),
     path('todo/paginate/<int:page>/', views.TodoList.as_view(), name='todo-paginate'),
     path('todo-groups/', views.TodoGroupList.as_view(), name='todo-group-list'),

     #register
     # path('register/', views.register.as_view(), name='register'),
     #
     # # #users
     # path ('user/', views.User.as_view(),name='user'),
     # # path ('user/<int:pk>', views.UserView.as_view()),
     # #
     # # #otp
     # path('otp/',views.OtpView.as_view(),name='otp'),
     # path('otp/<int:pk>',views.OtpView.as_view()),











     # #For Todos
     # path('todos/create/', views.TodoView.as_view({'post': 'create'}), name='todo-create'),
     # path('todos/list/', views.TodoView.as_view({'get': 'list'}), name='todo-list'),
     # path('todos/delete/<int:pk>', views.TodoView.as_view({'delete': 'destroy'}), name='todo-delete'),
     #
     # #For Users
     # path('login/', views.UserView.as_view({'post': 'login'}), name='user-login'),
     # path('users/create/', views.UserView.as_view({'post': 'create'}), name='user-create'),
     # path('users/update/<int:pk>', views.UserView.as_view({'put': 'update'}), name='user-update'),
     #
     # #For OTP
     # path('otp/create/', views.OtpView.as_view({'post': 'create'}), name='otp-create'),
     # path('otp/verify/', views.OtpView.as_view({'post': 'verify_otp'}), name='otp-verify'),
     # path('otp/reset_created_at/', views.OtpView.as_view({'post': 'reset_created_at'}), name='otp-reset-created-at'),


]