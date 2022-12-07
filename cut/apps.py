from django.apps import AppConfig


class CutConfig(AppConfig):
    name = 'cut'
    def ready(self):
        import cut.signals