import pytest

from bcjoy import app as bcjoy_app


@pytest.fixture
def app(request):
    """Flask application test fixture"""
    app_ = bcjoy_app.setup(
        TESTING=True
    )

    ctx = app_.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app_


@pytest.fixture
def test_client(app):
    return app.test_client()
