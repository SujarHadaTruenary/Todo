from django.urls import path
from . import views

urlpatterns  = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>/',views.completeTodo , name = 'complete'),
    path('verify',views.verify,name='verify'),
    path('register',views.register,name='register'),
    path('registerpage', views.registerPage, name='registerpage')

    # path('deletecomplete',views.deletecompleted ,name = 'deletecompleted'),
    # path ('deleteall',views.deleteall , name = 'deleteall')
]
