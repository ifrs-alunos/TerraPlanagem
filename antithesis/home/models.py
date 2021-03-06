from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

class Publicacao(models.Model):
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, verbose_name='Título')
	subtitle = models.CharField(max_length=200, verbose_name='Subtítulo', default='')
	text = models.TextField(verbose_name='Texto')
	image = models.ImageField(upload_to='media/', default='/media/discussion.gif', null=True,)

	def __str__(self):
		return self.title

class Comentario(models.Model):
	user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	publishing = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
	text = models.TextField()

	def __str__(self):
		return self.text
