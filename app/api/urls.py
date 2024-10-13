from api.views.api_check_identity_view import APICheckIdentityView
from api.views.api_create_identity_view import APICreateIdentityView
from django.urls import path

urlpatterns = [
    path("create-identity/", APICreateIdentityView.as_view(), name="api_create_identity"),
    path("check-identity/", APICheckIdentityView.as_view(), name="api_check_identity"),
]
