from sample_project.hello import hello


def test_hello():
    expected = "Hello World"
    result = hello()
    assert result == expected
