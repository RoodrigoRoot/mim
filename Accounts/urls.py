from django.urls import path
from .views import AccountsListCreateAPIView, AccountRetrieveUpdateDestroyAPIView, BenefitsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("api/v1/accounts/", AccountsListCreateAPIView.as_view(), name="accounts"),
    path("api/v1/accounts/<slug:slug>/", AccountRetrieveUpdateDestroyAPIView.as_view(), name="profile"),
    path("api/v1/accounts/<slug:slug>/benefits/", BenefitsRetrieveUpdateDestroyAPIView.as_view(), name="benefits"),
]
