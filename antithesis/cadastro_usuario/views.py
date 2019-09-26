from django.shortcuts import render
from home.models import Usuario

def cadastro_usuario(request):
	return render(request, 'cadastro_usuario/cadastro.html')
