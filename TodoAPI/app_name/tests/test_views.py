import json

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from app_name.models import *
from app_name.serializers import (
    TodoSerializer,
    DeadlineTodoSerializer,
    UserSerializer,
    LoginSerializer,
    OtpSerializer,
    ResetSerializer,
)

class TodoGroupListTestCase(APITestCase):
    def test_get_todo_group_list(self):

        todo.objects.create(name="Task 1", deadline="2023-12-31T23:59:59Z")
        todo.objects.create(name="Task 2", deadline="2023-12-31T23:59:59Z")

        response = self.client.get(reverse('todo-group-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoListTestCase(APITestCase):
    def test_get_todo_list(self):
        todo.objects.create(name="Task 1", deadline="2023-12-31T23:59:59Z")
        todo.objects.create(name="Task 2", deadline="2023-12-31T23:59:59Z")

        response = self.client.get(reverse('todo-paginate', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoViewTestCase(APITestCase):
    def test_get_todo(self):

        todo_item = todo.objects.create(name="Task 1", deadline="2023-12-31T23:59:59Z")
        response = self.client.get(reverse('todo-detail', args=[todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo(self):
        data = {'name': 'New Todo', 'deadline': '2023-12-31T23:59:59Z'}
        response = self.client.post(reverse('todo'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_todo(self):

        todo_item = todo.objects.create(name="UpdatedTodo", deadline="2023-12-31T23:59:59Z")
        data = {'name': 'UpdatedTodo', 'done': True ,'deadline':'2023-12-31T23:59:59Z'}
        response = self.client.put(reverse('todo-detail', args=[todo_item.id]), data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_todo(self):

        todo_item = todo.objects.create(name="Test Todo", deadline="2023-12-31T23:59:59Z")
        response = self.client.delete(reverse('todo-detail', args=[todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterTestCase(APITestCase):
    def test_register_user(self):
        data = {'email': 'test@example.com', 'uname': 'user', 'password': 'password'}
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTestCase(APITestCase):
    def test_user_login(self):

        user.objects.create(email='test@example.com', uname='user', password='password', verified=True)
        data = {'email': 'test@example.com', 'password': 'password'}
        response = self.client.post(reverse('user'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OtpViewTestCase(APITestCase):
    def test_post_otp(self):
        user.objects.create(email='test@example.com', uname='user', password='password', verified=False)
        otp_obj = otp.objects.create(email='test@example.com', code='123456')
        data = {'email': 'test@example.com', 'code': '123456'}
        response = self.client.post(reverse('otp'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_put_otp(self):

        otp_obj = otp.objects.create(email='test@example.com', code='123456')
        data = {'email': 'test@example.com', 'code': '654321'}
        response = self.client.put(reverse('otp'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
