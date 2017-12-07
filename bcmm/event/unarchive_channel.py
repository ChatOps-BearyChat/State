# -*- coding: utf-8 -*-


def on_unarchive_channel(store, message):
    data = message['data']
    channel_id = data['id']
    channel = store.get_channel_by_id(channel_id)
    channel.unarchive()
