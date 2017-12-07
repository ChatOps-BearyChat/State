# -*- coding: utf-8 -*-


def on_update_team(store, message):
    data = message.get('data', None)
    if store.team is not None and data is not None:
        store.team.update(**data)
