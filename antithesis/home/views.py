from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacao


def home(request):
	return HttpResponse(Publicacao.objects.all())


def publicacoes(request, publicacao_id):
	for publicacao in Publicacao.objects.all():
		if publicacao.id == publicacao_id:
			return HttpResponse(publicacao)
