# forms.py
from django import forms
from django .forms import ModelForm,FileInput
from .models import *

class OcrForm(forms.ModelForm):
	image = forms.ImageField(widget = forms.FileInput(attrs = {'class':'files'}))
	class Meta:
		model = Upload
		fields = "__all__"
