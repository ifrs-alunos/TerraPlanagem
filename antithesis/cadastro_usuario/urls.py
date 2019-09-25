from django.urls import path
from . import views

app_name = 'cadastro_usuario'

urlpatterns = [
	path('', views.cadastro_usuario, name='cadastro_usuario')
]
