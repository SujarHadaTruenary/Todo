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
    r = requests.get('http://127.0.0.1:8000/todo/', headers=headers)
    json_data = r.content
    data = json.loads(json_data)
    # todolist = [{"name": item["name"], "done": item["done"]} for item in data]

    form = TodoForm()
    context = {'todo_list': data, 'form': form}

    return render(request, 'todo/index.html', context)

    # return HttpResponse('hello')

   # todo_list = Todo.objects.order_by('id')


@require_POST
def addTodo(request):
    data = {"name": request.POST['text']}
    data_json = json.dumps(data)

    r = requests.post('http://127.0.0.1:8000/todo/', data=data_json, headers=headers)
    return redirect('index')

def completeTodo(request,todo_id):
    url = f'http://127.0.0.1:8000/todo/{todo_id}/'
    r = requests.delete(url, headers=headers)
    return redirect('index')


def login(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/user/'
        data = {
            'username': request.POST['userid'],
            'password': request.POST['password']
        }
        data_json = json.dumps(data)

        response = requests.get(url, data=data_json)
        response_data = response.json()
        if 'verified' in response_data and response_data['verified'] is True:
            return render(request, 'todo/index.html')
        else:
            context = {'Errors': "Not Verified"}
            return render(request, 'todo/login.html', context)

    else:
        return render(request, 'todo/login.html')

def registerPage(request):
    return render(request, 'todo/register.html')

def register(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/user/'
        data = {
            'email':request.POST['email'],
            'uname': request.POST['uname'],
            'password': request.POST['password'],
            'verified' : False
        }

        data_json = json.dumps(data)

        response = requests.post(url, data=data_json, headers=headers)

        code = random.randint(1000,9000)
        url2 = 'http://127.0.0.1:8000/otp/'
        data2 = {
            'email': request.POST['email'],
            'code' : code
        }
        data_json2 = json.dumps(data2)
        response2 = requests.post(url2, data=data_json2)
        print(code)

        return render(request, 'todo/verify.html')

    else:
        return render(request, 'todo/register.html')


def verify(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/otp/'
        data = {
            'email': request.POST['email'],
        }

        data_json = json.dumps(data)

        response = requests.get(url, params=data)

        response_data = json.loads(response.content)

        for sample in response_data:
         if 'code' in sample and str(sample['code']) == str(request.POST['code']):
            return render(request, 'todo/index.html')

         else :
            context = {'Error':"Not Verified"}
            return render(request, 'todo/verify.html',context)


    else:
        return render(request, 'todo/verify.html')




# def deletecompleted(request):
#     Todo.objects.filter(complete__exact=True).delete()
#
#     return redirect('index')
#
# def deleteall(request):
#     Todo.objects.all().delete()
#
#     return redirect('index')
