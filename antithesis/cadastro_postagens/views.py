from django.shortcuts import render, redirect, get_object_or_404
from cadastro_postagens.forms import PublicacaoForm
from login_usuario.forms import LoginForm
from home.models import Publicacao, Comentario

def cadastro_postagens(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PublicacaoForm(request.POST, request.FILES)
			
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
	if request.user.is_authenticated:
		publicacao = get_object_or_404(Publicacao, pk=publicacao_id)

		if request.method == 'POST':
			form = PublicacaoForm(request.POST, request.FILES, instance=publicacao)
			
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user.usuario
				post.save()

				return redirect('home')
		else:
			form = PublicacaoForm(instance=publicacao)

			dados = {
				'publicacao': publicacao,
				'form': form,
			}
			
			return render(request, 'cadastro_postagens/editar.html', dados)
	else:
		return redirect('home')

def deletar_postagem(request, publicacao_id):
	if request.user.is_authenticated:
		publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
		
		try:
			publicacao.delete()
		except:
			return render(request, 'cadastro_postagens/editar.html')

		return redirect('home')
	else:
		return redirect('home')

