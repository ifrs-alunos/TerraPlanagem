from django import forms
from home.models import Publicacao

class PublicacaoForm(forms.ModelForm):
	class Meta:
		model = Publicacao
		fields = ('title', 'text',)
		widgets = {
			'title': forms.TextInput(attrs={'autocomplete': 'off',}),
			'text': forms.Textarea(attrs={'autocomplete': 'off', 'class': 'materialize-textarea'}),
		}
