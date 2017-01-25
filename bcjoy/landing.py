"""
    bcjoy.landing
    ~~~~~~~~~~~~~

    Landing page.
"""

from flask import Blueprint
from flask import redirect
from flask import url_for


bp = Blueprint('landing', __name__)


@bp.route('/join', methods=['GET'])
def join():
    return 'foobar'


def setup(app):
    app.register_blueprint(bp, url_prefix='')

    @app.route('/', methods=['GET'])
    def site_root():
        return redirect(url_for('landing.join'))

    return app
