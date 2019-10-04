from django.shortcuts import render
from django.contrib.auth.models import User
from home.models import Usuario
from .forms import UserForm


def cadastro_usuario(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		
		if form.is_valid():
			user = form.save()

			Usuario(user=user).save()

			print(user)

			return render(request, 'login_usuario/login.html')
	else:
		form = UserForm()	
	
	return render(request, 'cadastro_usuario/cadastro.html', {'form': form})
