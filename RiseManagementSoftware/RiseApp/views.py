from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.
def index(request):
  return HttpResponse("Hello World! This is the Dashboard.")

def projects_list(request):
  return HttpResponse("This returns a list of projects")

def current_project(request):
  return HttpResponse("This is the current project being viewed")

def user_account(request):
  return HttpResponse("This returns the user_account")

def teams(request):
  return HttpResponse("This returns the team profile")

def user_creation(request):
  
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
       form.save()

  context={'form':form}
  return render(request, 'RiseApp/user_creation.html', context)

def user_login(request):
  return HttpResponse("This returns the login page")