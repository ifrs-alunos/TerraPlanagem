from django.urls import path
from . import views

app_name = 'cadastro_postagens'

urlpatterns = [
	path('', views.cadastro_postagens, name='cadastro_postagens'),
	path('editar_postagem/<int:publicacao_id>/', views.editar_postagem, name='editar_postagem'),
	path('deletar_postagem/<int:publicacao_id>/', views.deletar_postagem, name='deletar_postagem'),
	path('excluir_comentario/<int:comentario_id>/', views.excluir_comentario, name='excluir_comentario')
]
