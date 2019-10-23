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

	#def clean(self):
	#	cleaned_data = super().clean()

	#	if len(cleaned_data["password"]) < 8:
	#		self.add_error("password", "A senha precisa ter 8 ou mais caracteres")
