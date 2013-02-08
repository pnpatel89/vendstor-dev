from django import forms
import re
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	username = forms.CharField(max_length=30)
	email = forms.EmailField()
	password1 = forms.CharField(
		widget=forms.PasswordInput(),
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(),
	)
	Name = forms.CharField(max_length=30)
	radio_buttons = forms.ChoiceField(
		choices = (
		('option_one', "Buyer-I'm a business that wants to buy from vendors."),
		('option_two', "Vendor-I want to sell to businesses.")
		),
		widget = forms.RadioSelect,
		initial = 'option_two',
	)
	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
				raise forms.ValidationError('Passwords do not match.')
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only contain '
				'alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')

	