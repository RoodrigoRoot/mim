from django.shortcuts import render
from rest_framework import generics
from .models import Accounts, Benefits
from .serializers import AccountsSerializer, BenefitsSerializer

# Create your views here.

class AccountsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    lookup_field = "slug"

class BenefitsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Benefits.objects.all()
    
    def get_object(self):
        return Benefits.objects.get(user__slug=self.kwargs["slug"])
    
    serializer_class = BenefitsSerializer