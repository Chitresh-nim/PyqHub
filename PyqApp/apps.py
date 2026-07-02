from django.apps import AppConfig

class PyqappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PyqApp'

   # def ready(self):
        # import PyqApp.signals