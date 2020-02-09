from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = "home.html"
    if request.user.is_authenticated:
        context = {"name" :"Hello Ajay"}
    else: 
        context = {"name" : "unknown"}
    return render(request,template, context)