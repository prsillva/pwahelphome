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

