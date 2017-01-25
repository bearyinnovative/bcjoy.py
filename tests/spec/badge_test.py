def test_bearychat_badge_should_be_svg(test_client):
    resp = test_client.get('/badge/bearychat.svg')
    assert resp.status_code == 200
    assert resp.content_type == 'image/svg+xml'


def test_bearychat_badge_should_contain_bearychat(test_client):
    resp = test_client.get('/badge/bearychat.svg')
    assert 'BearyChat' in resp.data.decode('u8')
