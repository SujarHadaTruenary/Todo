from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Count
from .services import TodoListServices

# Create your views here.

#api view  for crud

class TodoGroupList(APIView):
    def get(self, request, format=None):
        # grouped_todos = todo.objects.values('deadline').annotate(
        #     todo_count=Count('id')
        # )
        #
        # todo_data = []
        # for group in grouped_todos:
        #     todos = todo.objects.filter(deadline=group['deadline'])
        #     todos_serialized = DeadlineTodoSerializer(todos, many=True).data
        #     todo_data.append({
        #         'deadline': group['deadline'],
        #         'todo_count': group['todo_count'],
        #         'todos': todos_serialized
        #     })

        todo_data = TodoListServices.grouped_by_deadline()

        serializer = TodoGroupSerializer(todo_data, many=True)
        return Response(serializer.data)







class TodoList(APIView):
    def get(self,request,page=None, format=None):

        todos = TodoListServices.list_todo_paginate(page)

        # page_number = page
        # page_size = 10
        # if page_number is None:
        #     page_number = 1
        #
        # todos = todo.objects.all()[
        #  (page_number - 1) * page_size: page_number * page_size
        #  ]

        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class TodoView(APIView):
    # queryset = todo.objects.all()
    # serializer_class = TodoSerializer
    def get(self, request,pk=None, format=None):
        id = pk
        if id is not None:
         todos = todo.objects.get(id = id)
         serializer = TodoSerializer(todos , context={'request': request})
         return Response(serializer.data, status=status.HTTP_200_OK)


        todos = TodoListServices.list_todo()
        serializer = TodoSerializer(todos, many=True , context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format = None):
        serializer = TodoSerializer(data=request.data , context={'request': request} )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk ):
        id = pk
        obj = todo.objects.get(pk = id)
        obj.delete()
        return Response({'msg':'Data Deleted'})

    def put (self, request,pk,format = None):
        id = pk
        obj = todo.objects.get(pk = id)
        serializer = TodoSerializer(obj,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete'},status=status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



    # def destroy(self, request, pk=None, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class register(APIView):
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#
#             otp_instance = otp.objects.create(email=serializer.validated_data['email'],code='123456')
#             otp_instance.save()
#
#             return Response({'msg':'Complete'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class User(APIView):
#
#     def post(self, request,format=None):
#         serializer = LoginSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         email = serializer.validated_data.get('email')
#         password = serializer.validated_data.get('password')
#
#         data = user.objects.get(email=email)
#
#         if not data:
#             return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if not data.password == password :
#             return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if not data.verified:
#             return Response({'error': 'User is not verified'}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(status=status.HTTP_200_OK)
#
#
# class OtpView(APIView):
#     def post(self, request,format=None):
#         serializer = OtpSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         email = serializer.validated_data.get('email')
#         code = serializer.validated_data.get('code')
#
#
#         obj = otp.objects.get(email=email, code=code)
#         if not obj:
#             return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if obj.created_at < timezone.now() - timezone.timedelta(seconds=10):
#             return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
#
#         object = user.objects.get(email=email)
#         object.verified = True
#         object.save()
#         return Response({'success': True}, status=status.HTTP_200_OK)
#
#     def put(self, request,format=None):
#         serializer = ResetSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         email = serializer.validated_data.get('email')
#         code = serializer.validated_data.get('code')
#         obj = otp.objects.get(email=email)
#         obj.code = code
#         obj.created_at = timezone.now()
#         obj.save()
#         return Response({'success': True}, status=status.HTTP_200_OK)
#
