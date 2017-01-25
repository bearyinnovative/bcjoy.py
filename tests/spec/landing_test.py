from urllib.parse import urlparse


def test_should_redirect_to_landing_page_on_root(test_client):
    resp = test_client.get('/', follow_redirects=False)
    assert urlparse(resp.location).path == '/join'
    assert resp.status_code == 302


def test_should_render_landing_page(test_client):
    resp = test_client.get('/join')
    assert resp.status_code == 200
