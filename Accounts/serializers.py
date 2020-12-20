from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        extra_kwargs = {
            'password': {'write_only': True}            
        }

class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Codes
        fields = ("code",)
        extra_kwargs = {
            'code': {'read_only': True}            
        }


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusUser
        fields = ("status",)

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ("id", "name",)

class AccountsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    codes = CodeSerializer(required=False)
    status = StatusSerializer(required=False)
    country = CountriesSerializer()

    class Meta:
        model = Accounts
        fields = ("id", "user", "phone", "country", "slug", "status", "birthday", "codes")
        extra_kwargs = {
            'slug': {'read_only': True}            
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["user"]["username"],
            first_name=validated_data["user"]["first_name"],
            last_name=validated_data["user"]["last_name"],
            email=validated_data["user"]["email"],
            password=validated_data["user"]["password"]
        )
        account = Accounts.objects.create(
            user=user,
            
        )
        return account
class BenefitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benefits
        fields = ("fullname",)