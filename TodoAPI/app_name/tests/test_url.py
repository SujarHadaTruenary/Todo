from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_name.views import *


class TestUrls(SimpleTestCase):

    def test_todo_url(self):
        url = reverse('todo')
        self.assertEqual(resolve(url).func.view_class, TodoView)

    def test_todo_detail_url(self):
        url = reverse('todo-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, TodoView)

    def test_todo_paginate_url(self):
        url = reverse('todo-paginate', args=[1])
        self.assertEqual(resolve(url).func.view_class, TodoList)

    def test_todo_group_list_url(self):
        url = reverse('todo-group-list')
        self.assertEqual(resolve(url).func.view_class, TodoGroupList)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, register)

    def test_user_url(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func.view_class, User)

    def test_otp_url(self):
        url = reverse('otp')
        self.assertEqual(resolve(url).func.view_class, OtpView)
