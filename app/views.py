from django.shortcuts import render,redirect
from django.contrib import messages

## import todo form and models

from .forms import TodoForm
from .models import Todo

##############################################

def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app')

    form = TodoForm()
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           }
    return render(request,'app/index.html',page)


### function to remove item , it receive todo item id from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    # if item_id is not None:
    #     id = item_id
    if request.method == "POST":
        item.delete()
        messages.info(request,"item removed !!!")
        return redirect('/')
    todo = {"todo": Todo.objects.get(id=item_id)}
    return render(request, 'delete.html', todo)


# def edit(request, item_id):
#
#     if request.method == "POST":
#         newtitle = request.POST.get('title')
#         newdesc = request.POST.get('details')
#
#         item = Todo.objects.get(id=item_id)
#
#         item.title = newtitle
#         item.details = newdesc
#
#         item.save()
#         messages.info(request, "Item edited")
#         return redirect("app")
#     item = Todo.objects.get(id=item_id)
#     context = {'title': item.title, 'details': item.details}
#     return render(request, 'edit.html', context)

def edit(request, item_id):
    form = TodoForm(request.POST, instance=Todo)
    task = Todo.objects.get(id=item_id)
    form = TodoForm(instance=Todo)
    context = {'form': form}

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=Todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit.html', context)