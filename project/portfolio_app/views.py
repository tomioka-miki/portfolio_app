from django.shortcuts import render, redirect
from .models import TodoList
from .forms import AddListForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AddListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = TodoList.objects.all
            return render(request, 'index.html', {'all_items': all_items})
    else:
        all_items = TodoList.objects.all
        return render(request, 'index.html', {'all_items': all_items})


def delete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.delete()
    return redirect('index')


def uncomplete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')


def complete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('index')


def edit(request, list_id, list_item):
    item = TodoList.objects.get(pk=list_id)
    print(list_item)
    item.item = list_item
    item.save()        
    return redirect('index')
