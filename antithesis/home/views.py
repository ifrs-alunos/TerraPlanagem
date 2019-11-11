from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Publicacao
from .forms import ComentarioForm

def home(request):
	publicacao_recente_lista = Publicacao.objects.order_by('-id')

	dados = {
		'publicacao_recente_lista': publicacao_recente_lista,
	}
	
	return render(request, 'home/index.html', dados)


def publicacao(request, publicacao_id):
	publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
	form = ComentarioForm()

	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ComentarioForm(request.POST)
			
			if form.is_valid():
				comentario = form.save(commit=False)
				comentario.user = request.user.usuario
				comentario.publishing = publicacao
				comentario.save()
				
				return redirect('home')
				
	dados = {
		'publicacao': publicacao,
		'form': form,
	}

	return render(request, 'home/publicacao.html', dados)
