"""
    bcjoy.team
    ~~~~~~~~~~

    BearyChat team realtime stats.
"""

import os
import threading
import time
import logging

import bearychat
from flask import g


POLL_INTERVAL_IN_MS = 2000


class Team(object):

    def __init__(self, team_config):
        self.rtm = bearychat.RTMClient(team_config['rtm_token'])
        self.invite_url = team_config['invite_url']

        self._lock = threading.RLock()
        self._info = {}
        self._members = []

    def update_info(self):
        info = self.rtm.current_team.info()
        if info is None or not info._data:
            return
        with self._lock:
            # hack for bearychat@0.2.0
            self._info = info._data

    def update_members(self):
        members = self.rtm.current_team.members()
        if not members:
            return
        with self._lock:
            # hack for bearychat@0.2.0
            self._members = [member for member in members]

    @property
    def count_total_members(self):
        with self._lock:
            return len([i for i in self._members if i.is_normal()])

    @property
    def count_online_members(self):
        with self._lock:
            return len([i for i in self._members
                        if i.is_online() and i.is_normal()])

    def __str__(self):
        return '{}'.format(self._info.get('subdomain', '<unknown>'))


def must_read_config(d):
    rtm_token = d['BCJOY_RTM_TOKEN']
    if not rtm_token:
        raise RuntimeError('BCJOY_RTM_TOKEN required')

    invite_url = d['BCJOY_INVITE_URL']
    if not invite_url:
        raise RuntimeError('BCJOY_INVITE_URL required')

    return {
        'rtm_token': rtm_token,
        'invite_url': invite_url,
    }


def spawn_polling(team, poll_interval_in_ms):

    def poll():
        while True:
            time.sleep(poll_interval_in_ms / 1000)

            logging.info('team {} update members start...'.format(team))
            team.update_members()
            logging.info('team {} update members finished...'.format(team))

    t = threading.Thread(target=poll)
    t.start()

    return t


def setup(app):
    team = Team(must_read_config(os.environ))

    polling_thread = spawn_polling(team, POLL_INTERVAL_IN_MS)

    @app.before_request
    def bind_team():
        g.bcjoy_team = team
        g.bcjoy_team_polling_thread = polling_thread

    return app
