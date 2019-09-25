from django.shortcuts import render

def cadastro_usuario(request):
	return render(request, 'cadastro_usuario/cadastro.html')
