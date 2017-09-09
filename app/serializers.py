from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'