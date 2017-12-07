# -*- coding: utf-8 -*-

from bcmm.model.channel import Channel


def on_channel_visible(store, message):
    data = message['data']
    channel = Channel(**data)
    store.add_channel(channel)
