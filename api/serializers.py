from copyreg import pickle

from core import models
from django.contrib.auth.models import User
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name','description']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ['name','categories']

class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = ['phone_number','user','type']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['user', 'picture', 'birth_date', 'gender', 'services', 'social_number','zip_code','street','number','complement', 'district', 'city', 'state']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Review
        fields = ['profile','user', 'title', 'comment', 'stars']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']