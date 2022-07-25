from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    msg_list = [
        {'name': '1', 'age': 10},
        {'name': '2', 'age': 13},
        {'name': '3', 'age': 15},
    ]
    msg_str = 'user info'
    a = 20
    return render(request, 'index.html', {'list': msg_list, 'str': msg_str, 'a': a})

def login(request):
    msg = {'info': ''}
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('password')
        if name == 'admin' and pwd == '3':
            return redirect('/app/index/')
        else:
            msg['info'] = 'error'
    return render(request, 'login.html', msg)