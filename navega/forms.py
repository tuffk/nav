from django.contrib.auth.models import User
from django import forms
from .models import Embarcacion

class UserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password']

class EmbarcacionForm(forms.ModelForm):

    class Meta:
        model = Embarcacion
        fields = ['nombre', 'eslora', 'calado', 'carga']