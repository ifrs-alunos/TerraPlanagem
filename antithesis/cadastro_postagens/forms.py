from django import forms
from home.models import Publicacao

class PublicacaoForm(forms.ModelForm):
	class Meta:
		model = Publicacao
		fields = ('title', 'subtitle', 'text',)
		widgets = {
			'title': forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control',}),
			'subtitle': forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control',}),
			'text': forms.Textarea(attrs={'autocomplete': 'off', 'class': 'form-control',}),
		}
