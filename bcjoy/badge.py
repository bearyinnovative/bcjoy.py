"""
    bcjoy.badge
    ~~~~~~~~~~~

    Badge pages.
"""

from flask import Blueprint
from flask import g
from flask import make_response


BEARYCHAT_TMPL = '''
<svg xmlns="http://www.w3.org/2000/svg" width="{t_width}" height="20">
  <rect rx="3" width="{t_width}" height="20" fill="#555"></rect>
  <rect rx="3"
        x="{l_width}"
        width="{l_width}"
        height="20"
        fill="{color}">
  </rect>
  <path d="M{l_width} 0h{sep}v20h-{sep}z"
        fill="{color}">
  </path>
  <g text-anchor="middle" font-family="Verdana" font-size="11">
    {team_text}
    {value_text}
  </g>
</svg>
'''

BEARYCHAT_TEXT_TMPL = '''
    <text fill="#010101" fill-opacity=".3" x="{x}" y="15">{text}</text>
    <text fill="#fff" x="{x}" y="14">{text}</text>
'''


def width(text):
    return len(text) * 7


pad = 8
sep = 4


bp = Blueprint('badge', __name__)


@bp.route('/bearychat.svg', methods=['GET'])
def bearychat_badge():
    title = 'BearyChat'
    if g.bcjoy_team.count_online_members > 0:
        value = '{}/{}'.format(
            g.bcjoy_team.count_online_members,
            g.bcjoy_team.count_total_members
        )
    else:
        value = '{}'.format(g.bcjoy_team.count_total_members)

    l_width = pad + width(title) + sep
    r_width = sep + width(value) + pad
    t_width = l_width + r_width
    t_text = BEARYCHAT_TEXT_TMPL.format(x=l_width / 2, text=title)
    v_text = BEARYCHAT_TEXT_TMPL.format(x=l_width + r_width / 2, text=value)
    badge = BEARYCHAT_TMPL.format(
        t_width=t_width, l_width=l_width, color='#85c158', sep=sep,
        team_text=t_text, value_text=v_text
    )

    resp = make_response(badge)
    resp.content_type = 'image/svg+xml'
    return resp


def setup(app):
    app.register_blueprint(bp, url_prefix='/badge')

    return app
