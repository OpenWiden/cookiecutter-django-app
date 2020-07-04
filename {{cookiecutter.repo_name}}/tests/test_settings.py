import pytest
from django.core.exceptions import ImproperlyConfigured

from {{ cookiecutter.app_name }} import settings as app_settings


def test_load_settings_success():
    app_settings.load_settings()


def test_missed_settings(settings):
    del settings.{{ cookiecutter.app_name | upper }}
    with pytest.raises(ImproperlyConfigured):
        app_settings.load_settings()


def test_settings_is_not_a_dict(settings):
    settings.{{ cookiecutter.app_name | upper }} = list()
    with pytest.raises(ImproperlyConfigured):
        app_settings.load_settings()
