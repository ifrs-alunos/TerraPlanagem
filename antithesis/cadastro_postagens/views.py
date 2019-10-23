from django.shortcuts import render, redirect
from cadastro_postagens.forms import PublicacaoForm
from login_usuario.forms import LoginForm

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
