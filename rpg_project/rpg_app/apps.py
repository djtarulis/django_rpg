from django.apps import AppConfig

class RpgAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpg_app'

    def ready(self):
        import rpg_app.signals