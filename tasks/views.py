from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Task
from .forms import taskForm

# class TaskListView(ListView):
#     model = Task
#     template_name = 'home.html'
#     login_url = 'login'


# class TaskDeleteView(DeleteView):  # new
#     model = Task
#     template_name = 'Task_delete.html'
#     success_url = reverse_lazy('home')
#     login_url = 'login'


# class TaskCreateView(LoginRequiredMixin, CreateView):
#     model = Task
#     # template_name = 'Task_new.html'
#     fields = ('tasks', 'body')
#     login_url = 'login'


def home_view(request):
    task_list = Task.objects.order_by('id')
    form = taskForm()
    context = {"task_list": task_list, "form": form}
    return render(request, "tasks/index.html", context)
    # return HttpResponse("asdf")
    
# print("woringasd")
@ require_POST
# print("Adsfa")
def addTask_view(request):

    form = taskForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        # obj.task_name = request.duration
        # obj.duration  = request.duration
        # obj.task_name  = request.task_name
        obj.save()
        # form.save()

    return redirect('home')


# def completeTask_view(request, task_id):
#     Task = Task.objects.get(pk = task_id)
#     Task.complete = True
#     Task.save()
#     return redirect('home')


@ require_POST
def delete_view(request, task_id):

    task = Task.objects.get(pk=task_id)
    # if Task.complete = True:
    task.delete()
    # Task.objects.filter(complete__exact = True).delete()
    return redirect('home')


def deleteAll_view(request):
    Task.objects.all().delete()
    return redirect('home')


# @ require_POST
def startTimer_view(request,task_id):
    task = Task.objects.get(pk=task_id)
    # print(Task.duration)
    context = {'task_duration': task.duration}
    task_list = Task.objects.order_by('id')
    form = taskForm()
    context = {"task_list": task_list, "form": form,
               'task_duration': task.duration, "task_id": task.id}
    return render(request, "tasks/index.html", context)
