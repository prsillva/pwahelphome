from core import models
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers
from django.contrib.auth.models import User

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Category.objects.all().order_by('name')
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Service.objects.all().order_by('name')
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhoneNumberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.PhoneNumber.objects.all().order_by('created')
    serializer_class = serializers.PhoneNumberSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Profile.objects.all().order_by('user')
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Review.objects.all().order_by('profile')
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = User.objects.all().order_by('first_name')
        else:
            queryset = User.objects.filter(pk=user.pk).all()
        return queryset

    