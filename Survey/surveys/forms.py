from django import forms
from .models import Poll
from django.contrib.auth.models import User

class Login(forms.Form):
	Username = forms.CharField()
	Password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class SurveyForm(forms.ModelForm): 
	class Meta:
		model = Poll
		fields =['Question','Option1','Option2','Option3']