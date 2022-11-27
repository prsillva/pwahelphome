from django.urls import path
from . import views
from .views import SearchResultsView, ProfileDetailView, SearchResultsPwaView, ProfileDetailViewPwa

urlpatterns = [

    
    path('', views.pwa, name='pwa'),
    path('procurar/', views.procurar, name='procurar'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profilepwa/', views.profilepwa, name='profile_pwa'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('pesquisa', SearchResultsPwaView.as_view(), name='search_results_pwa'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile_detail'),
    path('profilepwa/<int:pk>', ProfileDetailViewPwa.as_view(), name='profile_detail_pwa')

]
