from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = task.objects.all()

    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks':tasks,
        'form' : form
    }
    return render(request, "task.html",context)

def updateTask(request,pk):
    tasks = task.objects.get(id=pk)

    form = Taskform(instance=tasks)

    if request.method == 'POST':
        form = Taskform(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {
        'item' : item
    }
    return render(request,'delete_task.html',context)
