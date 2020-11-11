import json
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from .models import Task
from .forms import AddTask
# Create your views here.



def index(request):
    task_list = Task.objects.order_by('due_date')
    context = {'task_list': task_list}
    return render(request, 'todo/index.html', context)

def completed(request):
    task_list = Task.objects.order_by('due_date')
    context = {'task_list': task_list}
    return render(request, 'todo/completed.html', context)

def all(request):
    task_list = Task.objects.order_by('due_date')
    context = {'task_list': task_list}
    return render(request, 'todo/all.html', context)

def toggle_complete(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	task.complete = not task.complete
	task.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

def add_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
    	form = AddTask(request.POST)
        # check whether it's valid:
    	if form.is_valid():
        	task = Task(**form.cleaned_data)
        	task.save()
            # redirect to a new URL:
        	return redirect(index)

    # if a GET (or any other method) we'll create a blank form
    else:
    	form = AddTask()

    return render(request, 'todo/add.html', {'form': form})

def edit_task(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = AddTask(request.POST, instance=task)
        # check whether it's valid:
		if form.is_valid():
			form.save()
            # redirect to a new URL:
			return redirect(index)
	
	else:
		form = AddTask(instance=task)
		context = {
			"form":form,
			"task":task,
			}
		return render(request, "todo/edit.html", context)