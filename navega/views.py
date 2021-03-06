import datetime

from django.contrib.auth import authenticate, logout, login
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Embarcacion
from .forms import UserForm, EmbarcacionForm

from django.views.generic import View

def ceo(request):
    st = datetime.date(2016,1,1)
    en = datetime.date(2016,12,31)
    ships = Embarcacion.objects.filter(fecha__range=(st, en))
    return render(request, 'navega/ceo.html', {"ships":ships})

def cfo(request):
    st = datetime.date(2006, 1, 1)
    en = datetime.date(2016, 12, 31)
    ships = Embarcacion.objects.filter(fecha__range=(st, en))
    return render(request, 'navega/cfo.html', {"ships":ships})

def gman(request):
    ships = Embarcacion.objects.all()
    return render(request, 'navega/gman.html', {"ships":ships})

def logoutMethod(request):
    if not request.user.is_authenticated():
        raise Http404

    logout(request)
    return redirect('/')


def success_create(request):

    context = {
        'title': 'Información guardada',
        'message': 'Hemos guardado la información que nos has proporcionado'
    }

    return render(request, 'navega/letrero.html', context=context)


def insertarEmbarcacion(request):

    if not request.user.is_authenticated() or request.user.is_superuser:
        raise Http404

    if request.method == 'POST':
        form = EmbarcacionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            return redirect('/navega/success')
        else:
            return render(request, 'navega/embarcacion.html', {'form': form})

    form = EmbarcacionForm(None)

    return render(request, 'navega/embarcacion.html', {'form': form})


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
                login(request, user)
                return redirect('/')


        message = 'password o usuario inválido'
        return render(request, self.template, {'form': form, 'message': message})

    def get(self, request):

        if request.user.is_authenticated():
            raise Http404

        form = self.form_class(None)
        return render(request, self.template, {'form': form})

