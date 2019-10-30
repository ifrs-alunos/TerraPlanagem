from django.urls import path
from . import views

app_name = 'cadastro_postagens'

urlpatterns = [
	path('', views.cadastro_postagens, name='cadastro_postagens'),
	path('editar_postagem/<int:publicacao_id>/', views.editar_postagem, name='editar_postagem')
]
