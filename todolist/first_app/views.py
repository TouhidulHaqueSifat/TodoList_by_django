from django.shortcuts import render,redirect, get_object_or_404
from first_app.forms import Listview
from first_app.models import TodoList

# Create your views here.

def store_task(request):
    if request.method=="POST":
        form = Listview(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = Listview()
    return render(request, 'store_task.html', {'form':form})

def show_task(request):
    form = TodoList.objects.filter(completed = False)
    
    return render(request,'show_task.html', {"form":form})


def complete(request, id):
    form = get_object_or_404(TodoList, pk = id)
    form.completed = True
    form.save()
    return redirect('complete1')

def completed1(request):
    completed_task = TodoList.objects.filter(completed = True)
    return render(request, 'complete_task.html', {"form":completed_task})
    
def edit(request,id):
    list = TodoList.objects.get(pk = id)
    form = Listview(instance=list)
    if request.method == 'POST':
        form = Listview(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        return render(request,'store_task.html',{"form":form})

def delete(request, id):
    form = TodoList.objects.get( pk = id ).delete()
    return redirect('show_task')
