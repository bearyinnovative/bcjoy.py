import pytest

from flask import g

from bcjoy import app as bcjoy_app


class MockTeam(object):

    def __init__(self, name, subdomain, invite_url,
                 count_total_members, count_online_members):
        self.name = name
        self.subdomain = subdomain
        self.invite_url = invite_url
        self.count_total_members = count_total_members
        self.count_online_members = count_online_members


@pytest.fixture
def mock_team():
    return MockTeam('mock', 'mock', 'http://mock', 0, 0)


@pytest.fixture
def app(request, mock_team):
    """Flask application test fixture"""
    app_ = bcjoy_app.setup(
        TESTING=True
    )

    ctx = app_.app_context()
    ctx.push()

    g.bcjoy_team = mock_team

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app_


@pytest.fixture
def test_client(app):
    return app.test_client()
