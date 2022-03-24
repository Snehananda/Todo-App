from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from TodoApp.models import TodoList
import datetime

# Create your views here.
def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "create.html")

def display(request):
    return render(request, "display.html")

def update(request):
    return render(request, "update.html")

def delete(request):
    return render(request, "delete.html")

def create(request):
    return render(request, "update.html")

@csrf_exempt
def createEvent(request):
    todo_title = request.POST.get("title")
    todo_content = request.POST.get("descp")
    todo_duedate = request.POST.get("due-date")
    res="Creating Event.... \nOh.. Got an Error!!!!"
    f = "%Y-%m-%d"
    print(type(todo_duedate))
    due_date = datetime.datetime.strptime(todo_duedate, f).date()
    print(todo_title, todo_content, "No", todo_duedate, due_date)
    
    
    try:
        tlist = TodoList(title= todo_title, description= todo_content, status="No", due_date=due_date)
        tlist.save()
        res = "Created Event successfully"
    except Exception:
        res = "Failed to create Event"

    

    return HttpResponse("<h3>"+res+"</h3>")
    

def displayEvents(request):

    response = []
    
    try:
        tlist = TodoList.objects.all()
        for val in tlist:
            response.append(val)

    except Exception:
        print("Error")
        
    return render(request, "display.html", {'todolist': response})

@csrf_exempt
def updateEvent(request):
    todo_title = request.POST.get("title")
    todo_content = request.POST.get("descp")
    todo_status = request.POST.get("status")
    todo_duedate = request.POST.get("due-date")

    try:
        tlist = TodoList.objects.get(title=todo_title)

        if todo_content != '':
            tlist.description = todo_content
        if todo_status != '':
            tlist.status = todo_status
        if todo_duedate != '':
            due_date = datetime.datetime.strptime(todo_duedate, "%Y-%m-%d").date()
            tlist.due_date = due_date

        tlist.save()
        return HttpResponse("<h3>Event Updated Successfully</h3>")
    except Exception:
        return HttpResponse("<h3>Failed to Updated Event</h3>")

@csrf_exempt
def deleteEvent(request):
    todo_title = request.POST.get("title")

    try:
        tlist = TodoList.objects.get(title=todo_title)
        tlist.delete()
        return HttpResponse("<h3>Event Updated Successfully</h3>")
    except Exception:
        return HttpResponse("<h3>Failed to Updated Event</h3>")