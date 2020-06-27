def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repo_name": "Test Django App"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "Test Django App"
    assert result.project.isdir()
