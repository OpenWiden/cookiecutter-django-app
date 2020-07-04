def test_repo_name(cookies):
    repo_name = "django-test-app"
    result = cookies.bake(extra_context={"repo_name": repo_name})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == repo_name
    assert result.project.isdir()


def test_app_name(cookies):
    app_name = "test_app"
    result = cookies.bake(extra_context={"app_name": app_name})

    assert result.exit_code == 0, print(result.exception)
    assert result.exception is None

    # Test directory
    test_app_dir = result.project.join(app_name)
    assert test_app_dir.isdir()

    # Test apps.py
    apps_module_file = test_app_dir.join("apps.py")
    apps_module_text = apps_module_file.read()
    assert "TestAppConfig" in apps_module_text
    assert 'name = "test_app"' in apps_module_text
