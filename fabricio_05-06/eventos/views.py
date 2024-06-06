from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .forms import EventoForm
from .models import Evento

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user  # Definindo o usuário autenticado como criador do evento
            evento.save()
            return redirect('eventos:todos_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'eventos/detalhe_evento.html', {'evento': evento})

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/excluir_evento_confirm.html', {'evento': evento})


from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('eventos:todos_eventos')  # Redirecionar para a página de todos os eventos após o login
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'eventos/registration/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Faça o login para começar.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'eventos/register.html', {'form': form})

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


def todos_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/todos_eventos.html', {'eventos': eventos})