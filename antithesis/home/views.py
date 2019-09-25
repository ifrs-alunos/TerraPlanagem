from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publicacao


def home(request):
	publicacao_recente_lista = Publicacao.objects.order_by('-id')
	
	dados = {
		'publicacao_recente_lista': publicacao_recente_lista,
	}
	
	return render(request, 'home/index.html', dados)


def publicacao(request, publicacao_id):
	publicacao = get_object_or_404(Publicacao, pk=publicacao_id)

	dados = {
		'publicacao': publicacao,
	}

	return render(request, 'home/publicacao.html', dados)
