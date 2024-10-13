from auth_service.models import IdentityModel
from django.contrib import admin


@admin.register(IdentityModel)
class IdentityAdmin(admin.ModelAdmin):
    pass