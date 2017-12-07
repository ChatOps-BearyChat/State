# -*- coding: utf-8 -*-


def on_new_channel_member(store, message):
    data = message['data']
    channel_id = data['channel_id']
    uid = data['uid']
    channel = store.get_channel_by_id(channel_id)
    channel.add_member(uid)
