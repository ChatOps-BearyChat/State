# -*- coding: utf-8 -*-


def on_delete_file(store, message):
    data = message['data']
    file_id = data['id']
    store.delete_file(file_id)
