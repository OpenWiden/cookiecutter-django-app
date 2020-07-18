Cookiecutter Django App
=======================

.. image:: https://github.com/OpenWiden/cookiecutter-django-app/workflows/Tests/badge.svg
    :target: https://github.com/OpenWiden/cookiecutter-django-app/actions
    :alt: Build

Cookiecutter Django App allows you to build modern apps with pre-configured development environment.

Features
--------

* `Poetry <https://python-poetry.org/>`_ - packaging and dependencies manager.
* `GitHub actions <https://help.github.com/en/actions>`_ - CI / CD for GitHub.
* Testing with `pytest <https://docs.pytest.org/en/latest/>`_ and `tox <https://tox.readthedocs.io/en/latest/index.html#>`_.
* Code quality with `black <https://github.com/psf/black>`_ and `isort <https://github.com/timothycrosley/isort>`_.
* `Shpinx <https://www.sphinx-doc.org/en/master/index.html>`_ docs.

Getting started
---------------

1. Create new project::

    $ cookiecutter https://github.com/OpenWiden/cookiecutter-django-app
    repo_name [django-app-name]: django-gitlab-webhooks
    project_description [App for Django.]: Gitlab webhooks for Django.
    author [my_name_or_nick_name]: stefanitsky
    email [my_email@email.com]: stefanitsky.mozdor@gmail.com
    app_name [app_name]: gitlab_webhooks
    app_version [0.1.0]:
    app_config_name [GitlabWebhooksConfig]:

2. Register on `Codecov https://codecov.io/gh`_ and add `Repository Upload Token` from settings to GitHub repository secrets with name `CODECOV_TOKEN`.
3. Register on `PyPi <https://pypi.org/>`_, create API token and add it to GitHub repository secrets with name `PYPI_TOKEN`.
4. Change urls for badges in README.rst if it's required.
5. Create project repository on `GitHub <https://github.com/new>`_.
6. Push local repositoriy::

    $ git init
    $ git add .
    $ git commit -m ':tada: initial commit'
    $ git remote add origin https://github.com/{{cookiecutter.author}}/{{cookiecutter.repo_name}}.git
    $ git push -u origin master

7. Register on `Read the Docs <https://readthedocs.org/>`_ and add your repository for auto docs create.
