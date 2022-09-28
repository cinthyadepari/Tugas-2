import re
from turtle import title
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import redirect
from django.http import HttpResponse
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
import datetime
from todolist.models import Profile
from django.contrib.auth.models import User

@login_required(login_url='/wishlist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    print(data_task)
    if request.user.is_authenticated:
        print(request.user.username)
    else:
        print('Tidak ada User')
    context = {
        'list_task': data_task,
        'nama' : request.user,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)    

def show_xml(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Profile.objects.create(user = user)
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:list_task")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
            
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form_todolist=TaskForm()
    if request.method == 'POST':
        form_todolist = TaskForm(request.POST or None, request.FILES or None)
        print(form_todolist)
        if form_todolist.is_valid():
            task=form_todolist.save(commit=False)
            task.user=request.user
            task.save()
            print(request.user)
            messages.success(request, (f"Task berhasil dibuat"))
            return redirect('todolist:list_task')
        else:
             print("Form tidak valid")

    context = {
        'form_todolist' : form_todolist,
        'title' : "Tambah Task",     
        }
    return render(request, "create_task.html", context)