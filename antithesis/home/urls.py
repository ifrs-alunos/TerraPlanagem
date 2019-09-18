from django.urls import path
from . import views

urlpatterns = [
	path('<int:publicacao_id>/', views.publicacoes, name='publicacoes'),
	path('', views.home, name='home'),
]
