from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginForm

def login_usuario(request):
	logout(request)

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)

			if user is not None:
				login(request, user)

				return redirect('home')
			else:
				return render(request, 'login_usuario/login.html', {'form': LoginForm(), 'erro': 'O usuário não está cadastrado'})
	else:
		# caso o formulário não estiver vindo no método post,
		# será enviado um formulário para o usuário
		form = LoginForm()

	return render(request, 'login_usuario/login.html', {'form': form})
