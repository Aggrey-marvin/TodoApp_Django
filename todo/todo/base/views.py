from django.shortcuts import render, redirect

from base.forms import TaskCreateForm
from .models import Task

# Create your views here.
def index(request):
  tasks = Task.objects.filter(complete=False)
  
  context = {
    'tasks': tasks, 
  }
  return render(request, "base/tasks.html", context)

def addTask(request):
  form = TaskCreateForm()
  
  if request.method == 'POST':
    form = TaskCreateForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.user = request.user
      task.save()
      return redirect('index')
  
  context = {
    'form': form,
  }
  return render(request, "base/add_task.html", context)

def editTask(request, id):
  task = Task.objects.get(id=id)
  
  form = TaskCreateForm(instance=task)
  
  context = {
    'form': form,
  }
  
  if request.method == "POST":
    form = TaskCreateForm(request.POST, instance=task)
    if form.is_valid():
      task = form.save(commit=False)
      task.user = request.user
      task.save()
      return redirect("index")
  
  return render(request, "base/edit_task.html", context)

def completeTask(request, id):
  task = Task.objects.get(id=id)
  task.complete = True
  task.save()
  return redirect("index")