# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json
import time
import thread

import requests
import websocket

from bcmm.logging import logger
from bcmm.store import Store
from bcmm.model import Team, Channel, User
from bcmm.event.handler import create_event_handler


def try_load_json(data, default=None):
    try:
        return json.loads(data)
    except Exception:
        return default


class HubotService(object):

    DEFAULT_BASE_URL = 'https://api.bearychat.com/v1'

    def __init__(self, token, base_url=None):
        self.token = token
        self.base_url = base_url or self.DEFAULT_BASE_URL

    def _url(self, path, base_url=None):
        return '%s%s' % (base_url or self.base_url, path)

    @property
    def start_url(self):
        return self._url('/start', base_url="https://rtm.bearychat.com")

    @property
    def team_info_url(self):
        return self._url('/team.info')

    @property
    def channels_info_url(self):
        return self._url('/channel.list')

    @property
    def users_info_url(self):
        return self._url('/user.list')

    def start(self):
        resp = requests.post(self.start_url, json={'token': self.token})
        content = try_load_json(resp.content, {})
        if resp.status_code != 200:
            raise RuntimeError("Failed to get ws host %s" %
                               content.get('error'))

        ws_host = content['result']['ws_host']
        if ws_host is None:
            raise RuntimeError("Failed to get ws host, ws_host got None")
        return ws_host

    def team_info(self):
        resp = requests.get(self.team_info_url, params={'token': self.token})
        if resp.status_code != 200:
            raise RuntimeError("Failed to get team info")
        content = try_load_json(resp.content, {})
        return content

    def channels_info(self):
        resp = requests.get(self.channels_info_url,
                            params={'token': self.token})
        if resp.status_code != 200:
            raise RuntimeError("Failed to get channels info")
        content = try_load_json(resp.content, {})
        return content

    def users_info(self):
        resp = requests.get(self.users_info_url,
                            params={'token': self.token})
        if resp.status_code != 200:
            raise RuntimeError('Failed to get users info')
        content = try_load_json(resp.content, {})
        return content


class MagicMirror(object):

    def __init__(self, token=None, bg=True):
        self._service = HubotService(token)
        self.call_id = 0
        self.store = Store()
        self.handler = create_event_handler(self.store)

        self.prepare_store(token)

        if token is not None:
            self.start(token, bg)

    def prepare_team_info(self):
        team_info = self._service.team_info()
        self.store.set_team(Team(**team_info))
        logger.debug('Prepared team info')

    def prepare_channels_info(self):
        channels_info = self._service.channels_info()
        channels = [Channel(**data) for data in channels_info]
        for c in channels:
            self.store.add_channel(c)
        logger.debug('Prepared channels info')

    def prepare_users_info(self):
        users_info = self._service.users_info()
        users = [User(**data) for data in users_info]
        for u in users:
            self.store.add_user(u)
        logger.debug('Prepared users info')

    def prepare_store(self, token):
        self.prepare_team_info()
        self.prepare_channels_info()
        self.prepare_users_info()

    def start(self, token, bg):
        ws_host = self._service.start()

        ws = websocket.WebSocketApp(
                ws_host,
                on_open=self._on_open,
                on_message=self._on_message)
        self.call_id = 0
        if bg:
            thread.start_new_thread(ws.run_forever, ())
        else:
            ws.run_forever()
        return ws

    def _next_call_id(self):
        self.call_id = self.call_id + 1
        return self.call_id

    def _on_open(self, ws):
        logger.debug("Connected")

        def ping_loop(*args):
            call_id = self._next_call_id()
            while True:
                time.sleep(10)
                ping = {'type': 'ping', 'call_id': call_id}
                ws.send(json.dumps(ping))
        thread.start_new_thread(ping_loop, ())

    def _on_message(self, ws, payload):
        message = json.loads(payload)
        logger.debug('Received msg: %s' % message)
        self.handler.handle_message(message)

    def command(self, cmd):
        if cmd == 'team.info':
            print self.store.get_team().name

        if cmd == 'channels.count':
            print len(self.store.channels)

        if cmd == 'users.count':
            print len(self.store.users)
