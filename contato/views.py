from django.shortcuts import render
from django.http import HttpResponse

def contato (request):
    return render (request, 'contato/contato.html'),