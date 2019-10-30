from django.shortcuts import render, redirect, get_object_or_404
from cadastro_postagens.forms import PublicacaoForm
from login_usuario.forms import LoginForm
from home.models import Publicacao

def cadastro_postagens(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PublicacaoForm(request.POST)
			
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user.usuario
				post.save()
				
				return redirect('home')
		else:
			form = PublicacaoForm()

		return render(request, 'cadastro_postagens/postagem.html', {'form': form})
	return redirect('home')

def editar_postagem(request, publicacao_id):
	publicacao = get_object_or_404(Publicacao, pk=publicacao_id)

	dados = {
		'publicacao': publicacao,
	}

	return render(request, 'cadastro_postagens/editar.html', dados)
