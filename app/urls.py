"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from api import views

from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'phone-number', views.PhoneNumberViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'user', views.UserViewSet, basename='user')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')), # < allauth
    path('api/v1/', include(router.urls)),
    path('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

