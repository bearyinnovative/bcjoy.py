"""
    bcjoy.badge_page
    ~~~~~~~~~~~~~~~~

    Badge pages.
"""

from flask import Blueprint
from flask import g
from flask import make_response

from bcjoy.badge import bearychat as badge_bearychat


bp = Blueprint('badge', __name__)


@bp.route('/bearychat.svg', methods=['GET'])
def bearychat_badge():
    text = 'BearyChat'
    if g.bcjoy_team.count_online_members > 0:
        value = '{}/{}'.format(
            g.bcjoy_team.count_online_members,
            g.bcjoy_team.count_total_members
        )
    else:
        value = '{}'.format(g.bcjoy_team.count_total_members)

    resp = make_response(badge_bearychat.render(text, value))
    resp.content_type = 'image/svg+xml'
    return resp


def setup(app):
    app.register_blueprint(bp, url_prefix='/badge')

    return app
