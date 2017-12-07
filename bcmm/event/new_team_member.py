# -*- coding: utf-8 -*-

from .bcmm.model.user import User


def on_new_team_member(store, message):
    user = User(**message['data'])
    store.add_user(user)
