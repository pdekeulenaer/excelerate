from django import forms

class ActivateEmailForm(forms.Form):
	email = forms.EmailField(label='')
