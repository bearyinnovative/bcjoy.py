"""
    bcjoy.app
    ~~~~~~~~~

    Application setup.
"""

from flask import Flask

from bcjoy import landing


class App(Flask):
    """bcjoy application instance"""


def setup(**settings):
    """Instantiation an wsgi application instance.

    Args:
        **settings: extra config settings

    Returns:
        wsgi application
    """
    app = App(__name__)

    app.config.update(settings)

    # setup components
    app = landing.setup(app)

    return app
