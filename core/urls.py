from django.urls import path
from . import views

from django.urls import path
from .views import *

urlpatterns = [

    path('', views.home, name='home'),
    path('pwa', views.pwa, name='pwa'),
    path('procurar/', views.procurar, name='procurar'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profilepwa/', views.profilepwa, name='profile_pwa'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('pesquisa', SearchResultsPwaView.as_view(), name='search_results_pwa'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile_detail'),
    path('profilepwa/<int:pk>', ProfileDetailViewPwa.as_view(), name='profile_detail_pwa'),
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('deslogar_usuario', deslogar_usuario, name="deslogar_usuario"),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario")

]
