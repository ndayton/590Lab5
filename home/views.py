from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! You’re at the home index. I'm testing CodeDeploy changes and I hope they work.")

