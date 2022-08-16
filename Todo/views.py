from asyncio import tasks
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


def update_task(request):
    return render(request, 'Todo/update_task.html')
