from django.apps import AppConfig


class AuthServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_service"

    def ready(self) -> None:
        from auth_service.models import (
            IdentityModel,
        )
        from auth_service.admin import (
            IdentityAdmin,
        )
        