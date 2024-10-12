from django.contrib import admin
from auth_service.models import IdentityModel


@admin.register(IdentityModel)
class IdentityAdmin(admin.ModelAdmin):
    pass