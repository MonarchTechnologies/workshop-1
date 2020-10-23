from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index():
  return HttpResponse("Hello World! This is the Dashboard.")

def projects_list():
  return HttpResponse("This returns a list of projects")

def current_project():
  return HttpResponse("This is the current project being viewed")

def user_account():
  return HttpResponse("This returns the user_account")
def teams():
  return HttpResponse("This returns the team profile")

def user_login():
  return HttpResponse("This returns the login page")