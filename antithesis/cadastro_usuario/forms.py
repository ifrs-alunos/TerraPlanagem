from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'email', 'password']
		widgets = {
			'username': forms.TextInput(
				attrs={
					'autocomplete': 'off',
					'class': 'form-control',
				}),
			'first_name': forms.TextInput(
				attrs={
					'autocomplete': 'off',
					'class': 'form-control',
				}),
			'email': forms.EmailInput(
				attrs={
					'autocomplete': 'off',
					'class': 'form-control',
				}),
			'password': forms.PasswordInput(
				attrs={
					'autocomplete': 'off',
					'class': 'form-control',
				}),
		}
