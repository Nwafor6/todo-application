from django.shortcuts import render, redirect
from .models import TodoApp



# Create your views here.

def homepage(request):
    if request.method=="POST":
        name=request.POST["name"]
        try:
            completed=request.POST["completed"]
        except:
            completed=False
        if completed == 'on':
            todoapp=TodoApp.objects.create(name=name,completed=True)
        else:
            todoapp=TodoApp.objects.create(name=name)
    todoapp=TodoApp.objects.all()
    return render(request, "index.html", {"todolist":todoapp})

def deleteitem(request, pk):
    todoapp=TodoApp.objects.get(id=pk)
    todoapp.delete()
    print("Deleted")
    todoapp=TodoApp.objects.all()

    return redirect("home")


def updateitem(request, id):  
    todoapp = TodoApp.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        completed = request.POST.get("completed", False)
        try:
            completed = bool(completed)
        except ValueError:
            completed = False
        if todoapp.completed == False and completed == True:
            todoapp.completed = True

        else:
            todoapp.completed = False

        todoapp.name = name
        todoapp.save()
        return redirect("home")
    return render(request, "update.html", {"item": todoapp,"name":todoapp.name})



# def updateitem(request, pk):
#     todoapp = TodoApp.objects.get(id=pk)
#     if request.method == "POST":
#         name = request.POST.get("name")
#         completed = request.POST.get("completed", False)
#         try:
#             completed = bool(completed)
#         except ValueError:
#             completed = False

#         if todoapp.completed == False and completed == True:
#             todoapp.completed = True
#         else:
#             todoapp.completed = False
#         todoapp.name = name
#         todoapp.save()
#         return redirect("home")
#     return render(request, "update.html", {"item": todoapp,"name":todoapp.name})


