from django.contrib import admin
from .models import Usuario, Publicacao, Comentario

admin.site.register(Publicacao)
admin.site.register(Comentario)
