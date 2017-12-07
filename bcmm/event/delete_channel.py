# -*- coding: utf-8 -*-


def on_delete_channel(store, message):
    data = message['data']
    channel_id = data['id']
    store.remove_channel(channel_id)
