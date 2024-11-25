from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def app2_fun(request):
    x = 10
    y = 20
    z = x + y

    return HttpResponse(f"<h1> sum of numbers {z} </h1>")
