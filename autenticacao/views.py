from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    # if request.method == 'GET':
    # return HttpResponse('aaaaaaaaaaa')
    return render(request, 'cadastro.html')
    

def logar(request):
    pass