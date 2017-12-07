# -*- coding: utf-8 -*-

from bcmm.model.file import File


def on_update_file(store, message):
    data = message['data']
    file_ = File(**data)
    store.add_file(file_)
