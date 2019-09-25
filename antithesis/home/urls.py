from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('<int:publicacao_id>/', views.publicacao, name='publicacao'),
	path('', views.home, name='home'),
]
