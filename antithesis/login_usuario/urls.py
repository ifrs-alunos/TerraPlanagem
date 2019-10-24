from django.urls import path
from . import views

app_name = 'login_usuario'

urlpatterns = [
	path('', views.login_usuario, name='login_usuario'),
	path('deslogar/', views.deslogar_usuario, name='deslogar_usuario')
]

