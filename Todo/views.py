from asyncio import tasks
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Todo/list.html', context)


def update_task(request, pk):
    task = Todo.objects.get(id=pk)

    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'Todo/update_task.html', context)


def deleteTask(requset, pk):
    item = Todo.objects.get(id=pk)

    if requset.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(requset, 'Todo/delete.html', context)
