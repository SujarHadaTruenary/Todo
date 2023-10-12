import json
import random
from .form import TodoForm
from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST
import requests

# Create your views here.
# token = ""


headers = {
    'Content-Type': 'application/json'
}

def index(request):
    r = requests.get('http://127.0.0.1:8000/', headers=headers)
    json_data = r.content
    data = json.loads(json_data)

    # todolist = [{"name": item["name"], "done": item["done"]} for item in data]

    form = TodoForm()
    context = {'todo_list': data, 'form': form}

    return render(request, 'todo/index.html', context)

    # return HttpResponse('hello')

   # todo_list = Todo.objects.order_by('id')


def addTodo(request):
    data = {
        "name": request.POST['text'],
        "deadline" : request.POST['deadline']
    }

    data_json = json.dumps(data)

    r = requests.post('http://127.0.0.1:8000/', data=data_json, headers=headers)
    return redirect('index')

def completeTodo(request,todo_id):
    url = f'http://127.0.0.1:8000/todo/{todo_id}'
    r = requests.delete(url)
    return redirect('index')


def login(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/user/'
        data = {
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        data_json = json.dumps(data)

        response = requests.post(url, data=data_json , headers = headers)

        if response.status_code == 200:
            return render(request, 'todo/index.html')
        else:
            try:
                response_data = response.json()
                first_key, first_value = next(iter(response_data.items()))
                error_message = f'{first_key}: {first_value}'
                context = {'Error': error_message}
                return render(request, 'todo/login.html', context)

            except Exception as e:
                context = {'Error': "Invalid Inputs "}
                return render(request, 'todo/login.html', context)

    else:
        return render(request, 'todo/login.html')

def registerPage(request):
    return render(request, 'todo/register.html')

def register(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/register/'
        data = {
            'email':request.POST['email'],
            'uname': request.POST['uname'],
            'password': request.POST['password'],
            'verified' : False
        }

        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers=headers)

        return render(request, 'todo/verify.html')

    else:
        return render(request, 'todo/register.html')


def verify(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/otp/'
        data = {
            'email': request.POST['email'],
            'code': request.POST['code'],
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers=headers)
        response_data = response.json()
        print(response_data)

        if 'success' in response_data and response_data['success'] is True:
            return render(request, 'todo/index.html')
        else:
            error_message = response_data.get('error', 'Not Verified')
            context = {'Error': error_message}
            return render(request, 'todo/verify.html', context)

    else:
        return render(request, 'todo/verify.html')



def resendcode(request):
    if request.method == 'POST':
       code = random.randint(1000, 9000)
       url = 'http://127.0.0.1:8000/otp/'
       data = {
              'email': request.POST['email'],
              'code': 1234567,
       }
       data_json = json.dumps(data)
       response = requests.put(url, data=data_json, headers=headers)
       print(code)
       return render(request, 'todo/verify.html')

    else:
       return render(request, 'todo/resendcode.html')

# def deletecompleted(request):
#     Todo.objects.filter(complete__exact=True).delete()
#
#     return redirect('index')
#
# def deleteall(request):
#     Todo.objects.all().delete()
#
#     return redirect('index')
