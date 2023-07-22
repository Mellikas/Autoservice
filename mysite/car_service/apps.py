from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_service'

    def ready(self):
        from .signals import create_profile, save_profile
