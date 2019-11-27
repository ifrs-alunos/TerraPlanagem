from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('<int:publicacao_id>/', views.publicacao, name='publicacao'),
	path('excluir_comentario/<int:comentario_id>/<int:publicacao_id>', views.excluir_comentario, name='excluir_comentario')
]
