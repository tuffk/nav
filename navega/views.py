from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import render, redirect
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

        if user is not None:

            if user.is_active:
                return redirect('/')


        message = 'password o usuario inválido'
        return render(request, self.template, {'form': form, 'message': message})

    def get(self, request):

        if request.user.is_authenticated():
            raise Http404

        form = self.form_class(None)
        return render(request, self.template, {'form': form})

