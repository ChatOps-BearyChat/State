# -*- coding: utf-8 -*-


def on_channel_invisible(store, message):
    data = message['data']
    channel_id = data['id']
    store.remove_channel(channel_id)
