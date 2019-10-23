from django.shortcuts import render
from django.contrib.auth.models import User
from home.models import Usuario
from .forms import UserForm
from login_usuario.forms import LoginForm


def cadastro_usuario(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()

			Usuario(user=user).save()

			return render(request, 'login_usuario/login.html', {'form': LoginForm()})
	else:
		form = UserForm()	
	
	return render(request, 'cadastro_usuario/cadastro.html', {'form': form})
