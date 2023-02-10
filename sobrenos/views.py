from django.shortcuts import render
from django.http import HttpResponse

def sobrenos (request):
    #return render(request, 'sobrenos.html')
    return HttpResponse('CARALHO')
