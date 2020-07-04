from django.apps import AppConfig


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = "{{ cookiecutter.app_name }}"

    def ready(self):
        from . import settings

        settings.load_settings()
