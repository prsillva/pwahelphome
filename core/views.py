from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.template import loader
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile, Review
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro_user.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login_site.html', {'form_login': form_login})

@login_required(login_url='/logar_usuario')
def deslogar_usuario(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/logar_usuario')
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})



def home(request):
        usuario = Profile.objects.all()
        servicos = Review.objects.all()
        template = loader.get_template('core/home.html')
        context = {
        'usuario': usuario,
        'servicos':servicos,
        }
        return new_func(request, template, context)

def pwa(request):
        usuario = Profile.objects.all()
        servicos = Review.objects.all()
        template = loader.get_template('core/pwa.html')
        context = {
        'usuario': usuario,
        'servicos':servicos,
        }
        return new_func(request, template, context)



def new_func(request, template, context):
    return HttpResponse(template.render(context, request))
    
def procurar(request):
    return render(request, 'core/procurar.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'core/profile.html', context)

@login_required
def profilepwa(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'core/profile_pwa.html', context)


class SearchResultsView(ListView):
    model = Profile
    paginate_by = 3
    template_name = 'core/search_results.html'


    def get_queryset(self):
        estado = self.request.GET.get('uf')
        cidade = self.request.GET.get('cidade')
        search = self.request.GET.get('search')
        return Profile.objects.filter(
            Q(state__icontains=estado) & Q(city__icontains=cidade) & Q(services__name__icontains=search)
        )

class SearchResultsPwaView(ListView):
    model = Profile
    paginate_by = 3
    template_name = 'core/search_results_pwa.html'


    def get_queryset(self):
        estado = self.request.GET.get('uf')
        cidade = self.request.GET.get('cidade')
        search = self.request.GET.get('search')
        return Profile.objects.filter(
            Q(state__icontains=estado) & Q(city__icontains=cidade) & Q(services__name__icontains=search)
        )


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'core/profile_detail.html'

class ProfileDetailViewPwa(DetailView):
    model = Profile
    template_name = 'core/profile_detail_pwa.html'

