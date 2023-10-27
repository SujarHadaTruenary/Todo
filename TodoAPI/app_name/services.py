from .models import todo
from .serializers import TodoSerializer , DeadlineTodoSerializer
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination


class TodoListServices:
    def list_todo_paginate( page ):

        page_number = page
        page_size = 10
        if page_number is None:
            page_number = 1

        todos = todo.objects.all()[
                (page_number - 1) * page_size: page_number * page_size
                ]

        return todos

    def grouped_by_deadline(self):
        grouped_todos = todo.objects.values('deadline').annotate(
            todo_count=Count('id')
        )

        todo_data = []
        for group in grouped_todos:
            todos = todo.objects.filter(deadline=group['deadline'])
            todos_serialized = DeadlineTodoSerializer(todos, many=True).data
            todo_data.append({
                'deadline': group['deadline'],
                'todo_count': group['todo_count'],
                'todos': todos_serialized
            })

        return todo_data

# class TodoFunctions:
#
#     def gettodo(self,request,id):
#         todos = todo.objects.get(id=id)
#         serializer = TodoSerializer(todos, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)


