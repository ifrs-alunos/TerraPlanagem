from django import forms
from home.models import Comentario

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ('text',)
		widgets = {
			'text': forms.Textarea(attrs={'autocomplete': 'off', 'class': 'form-control', 'rows': '4', 'cols': '50'}),
		}
