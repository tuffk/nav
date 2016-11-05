from django.shortcuts import render
from .models import Embarcacion
from .forms import UserForm

from django.views.generic import View

# Create your views here.
class UserLoginView(View):

    template = 'navega/login.html'
    form_class = UserForm

    def post(self, request):
        form = self.form_class(data={'email': self.request.POST['email'],
                                     'password': self.request.POST['password']})

    email = self.request.POST['email']
    password = self.request.POST['password']

    # aquí se hace el query en la base de datos para autentificar al usuario
    user = authenticate(username=email, password=password)