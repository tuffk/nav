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

    TIPO = (('Pasajero', 'Pasajero'), ('Carga', 'Carga'))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    eslora = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    calado = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=TIPO, label='Tipo')
    carga = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    costo = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Embarcacion
        fields = ['nombre', 'eslora', 'calado', 'tipo', 'carga', 'costo']