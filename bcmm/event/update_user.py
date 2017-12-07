# -*- coding: utf-8 -*-


def on_update_user(store, message):
    data = message.get('data', None)
    user_id = data['id']
    user = store.get_user_by_id(user_id)
    if user is not None and data is not None:
        user.update(**data)
