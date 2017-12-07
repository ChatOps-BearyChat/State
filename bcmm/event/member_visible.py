# -*- coding: utf-8 -*-


def on_member_visible(store, message):
    data = message['data']
    user_id = data['id']
    user = store.get_user_by_id(user_id)
    user.unarchive()
