from django.shortcuts import render
from django.http import HttpResponse

def estatico (request):
    return render(request,'estatico/estatico.html')