from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Publicacao
from .forms import ComentarioForm
from .models import Comentario

def home(request):
	publicacao_recente_lista = Publicacao.objects.order_by('-id')
	paginator = Paginator(publicacao_recente_lista, 3)

	page = request.GET.get('page')
	publicacoes = paginator.get_page(page)

	dados = {
		'publicacao_recente_lista': publicacoes,
	}
	
	return render(request, 'home/index.html', dados)


def publicacao(request, publicacao_id):
	publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
	form = ComentarioForm()
	mensagens = ""

	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ComentarioForm(request.POST)
			
			if form.is_valid():
				comentario = form.save(commit=False)
				comentario.user = request.user.usuario
				comentario.publishing = publicacao
				comentario.save()
	else:
		mensagens = "Você não está logado para fazer um comentário!"

	dados = {
		'publicacao': publicacao,
		'form': form,
		'mensagens': mensagens,
	}

	return render(request, 'home/publicacao.html', dados)

def excluir_comentario(request, comentario_id, publicacao_id):
	if request.user.is_authenticated:
		comentario = get_object_or_404(Comentario, pk=comentario_id)
		
		try:
			comentario.delete()
		except:
			pass

	publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
	form = ComentarioForm()
	mensagens = ""

	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ComentarioForm(request.POST)
			
			if form.is_valid():
				comentario = form.save(commit=False)
				comentario.user = request.user.usuario
				comentario.publishing = publicacao
				comentario.save()
	else:
		mensagens = "Você não está logado para fazer um comentário!"

	dados = {
		'publicacao': publicacao,
		'form': form,
		'mensagens': mensagens,
	}

	return render(request, 'home/publicacao.html', dados)
