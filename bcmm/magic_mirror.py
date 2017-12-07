# -*- coding: utf-8 -*-

import json
import time
import thread

import requests
import websocket

from bcmm.logging import logger
from bcmm.store import Store
from bcmm.event.handler import create_event_handler


def try_load_json(data, default=None):
    try:
        return json.loads(data)
    except Exception:
        return default


class Service(object):

    DEFAULT_BASE_URL = 'https://rtm.bearychat.com'

    def __init__(self, base_url=None):
        self.base_url = base_url or Service.DEFAULT_BASE_URL

    @property
    def start_url(self):
        return '%s/start' % self.base_url


service = Service()


class MagicMirror(object):

    def __init__(self, token=None):
        self.call_id = 0
        self.store = Store()
        self.handler = create_event_handler(self.store)

        if token is not None:
            self.start(token)

    def start(self, token):
        url = service.start_url
        resp = requests.post(url, json={'token': token})
        content = try_load_json(resp.content, {})
        if resp.status_code != 200:
            raise RuntimeError("Failed to get ws host %s" %
                               content.get('error'))

        ws_host = content['result']['ws_host']
        if ws_host is None:
            raise RuntimeError("Failed to get ws host, ws_host got None")

        ws = websocket.WebSocketApp(
                ws_host,
                on_open=self._on_open,
                on_message=self._on_message)
        self.call_id = 0
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
        print message
        self.handler.handle_message(message)
