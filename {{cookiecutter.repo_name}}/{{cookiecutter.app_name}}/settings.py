from django.conf import ImproperlyConfigured
from django.conf import settings as django_settings


def load_settings() -> None:
    try:
        settings = django_settings.{{ cookiecutter.app_name | upper }}
    except AttributeError:
        raise ImproperlyConfigured("{{ cookiecutter.app_name | upper }} settings is missing!")

    if not isinstance(settings, dict):
        raise ImproperlyConfigured("{{ cookiecutter.app_name | upper }} is not a dict!")

    # Your settings goes here ...
    # if "ALLOWED_EVENTS" not in settings:
    #     settings["ALLOWED_EVENTS"] = ["test"]
