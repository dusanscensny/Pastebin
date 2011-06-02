from django import forms
from pastebin.pasteapp.models import Pastebin

class PasteForm(forms.Form):
	nick = forms.CharField(max_length=20)
	date = forms.DateField()
	textTitle = forms.CharField(max_length=120)
	pasteText = forms.Textarea()
	expireDate = forms.DateTimeField()