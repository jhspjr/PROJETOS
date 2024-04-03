from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'orientacoes/home.html')

def defesas(request):
    return render(request, 'me-apague/temp.html')

def papers(request):
    return HttpResponse('papers OK')
# Create your views here.
