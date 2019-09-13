from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

class Publicacao(models.Model):
	user = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.title

class Comentario(models.Model):
	user = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
	publishing = models.ForeignKey(Publicacao, on_delete=models.SET_NULL, null=True)
	text = models.TextField()

	def __str__(self):
		return self.text