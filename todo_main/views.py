from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at')
    # tasks1 = Task.objects.filter(is_completed=True)
    # tasks2 = Task.objects.all()
    # tasks3 = Task.objects.get(id=1)
    # print(tasks)
    # print(tasks1)
    # print(tasks2)
    # print(tasks3)
    context = {
        "tasksForTemplate":tasks,
        "completed_task":completed_task,
    }
    return render(request, 'home.html',context)