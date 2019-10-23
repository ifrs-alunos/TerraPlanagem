from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control',}), label='Usuario')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off', 'class': 'form-control',}), label='Senha')
