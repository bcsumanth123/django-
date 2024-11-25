from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(f"<h1> this is app1 in the practice 5 functions</h1>")


def apps_fun(request):
    return HttpResponse(f"<h1> this is app1 in the practice 5 and apps to the sub in the numberfunctions</h1>")