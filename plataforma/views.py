from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovei

# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    imoveis = Imovei.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})