from django.shortcuts import render
from cadastro_postagens.forms import PublicacaoForm


def cadastro_postagens(request):
	if request.method == 'POST':
		form = PublicacaoForm(request.POST)
		
		if form.is_valid():
			

			return render(request, 'login_usuario/login.html', {'form': LoginForm()})
	else:
		form = PublicacaoForm()

	return render(request, 'cadastro_postagens/postagem.html', {'form': form})
