from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, status_choices
from .forms import TaskForm


def index(request, *args, **kwargs):

    tasks = Task.objects.all().order_by('-date')
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context)


def new(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        context = {
            'statuses': status_choices,
            'form': form
        }
        return render(request, 'new.html', context)

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.create(
                description=form.cleaned_data['description'],
                full_description=form.cleaned_data['full_description'],
                status=form.cleaned_data['status'],
                date=form.cleaned_data['date'],
            )
            return redirect('index')
        else:
            return render(request, 'new.html', context={'form': form})


def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'detail.html', context)


def delete(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        context = {
            'task': task
        }
        return render(request, 'delete.html', context)
    else:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'full_description': task.full_description,
            'status': task.status,
            'date': task.date
        })
        return render(request, 'edit.html', context={'form': form, 'task': task})

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.full_description = form.cleaned_data['full_description']
            task.status = form.cleaned_data['status']
            task.date = form.cleaned_data['date']
            task.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', context={'form': form, 'task': task})


def delete_items(request):
    data = request.POST
    for pk in data.keys():
        if pk == 'csrfmiddlewaretoken':
            continue
        task = get_object_or_404(Task, pk=pk)
        task.delete()
    return redirect('index')
