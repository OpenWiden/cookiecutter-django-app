import pytest


# FIXME: No module named 'tests.test_app' (but app tests works after app create)
@pytest.mark.skip
def test_run(cookies):
    repo_name = "test_django_app"
    result = cookies.bake(extra_context={"repo_name": repo_name})

    with result.project.join(repo_name).dirpath().as_cwd():
        tests_result = pytest.main()
        assert tests_result == tests_result.OK
