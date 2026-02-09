from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Tasks

def home(request):
    taskss = Tasks.objects.filter(is_completed = False)
    completed_task = Tasks.objects.filter(is_completed = True)
    context = {
        'taskss':taskss,
        'completed_task':completed_task
    }
    return render(request,'home.html',context)