import os

from bcjoy import app


def setup_leancloud():
    import leancloud
    from leancloud_cloud import engine

    leancloud.init(
        os.environ['LEANCLOUD_APP_ID'],
        app_key=os.environ['LEANCLOUD_APP_KEY'],
        master_key=os.environ['LEANCLOUD_APP_MASTER_KEY']
    )
    leancloud.use_master_key(False)

    return engine


application = None


if 'LEANCLOUD_APP_ID' in os.environ:
    application = setup_leancloud()
else:
    application = app.setup()
