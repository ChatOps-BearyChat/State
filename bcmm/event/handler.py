# -*- coding: utf-8 -*-

from bcmm.logging import logger


class EventHandler(object):

    def __init__(self, store):
        self.store = store
        self.callbacks = {}

    def on(self, event, cb):
        if event in self.callbacks:
            logger.warning('Cannot Overriding event handler "%s"' % event)

        self.callbacks[event] = cb

    def handle_message(self, message):
        event = message['type']
        cb = self.callbacks.get(event, None)
        if cb is None:
            logger.warning('Cannot find handler for event "%s"' % event)
            return
        return cb(self.store, message)


def create_event_handler(store):
    handler = EventHandler(store)

    from .update_team import on_update_team
    handler.on('update_team', on_update_team)

    from .update_user import on_update_user
    handler.on('update_user', on_update_user)

    from .channel_visible import on_channel_visible
    handler.on('channel_visible', on_channel_visible)

    from .channel_invisible import on_channel_invisible
    handler.on('channel_invisible', on_channel_invisible)

    from .update_channel import on_update_channel
    handler.on('update_channel', on_update_channel)

    from .archive_channel import on_archive_channel
    handler.on('archive_channel', on_archive_channel)

    from .unarchive_channel import on_unarchive_channel
    handler.on('unarchive_channel', on_unarchive_channel)

    from .delete_channel import on_delete_channel
    handler.on('delete_channel', on_delete_channel)

    from .new_robot import on_new_robot
    handler.on('new_robot', on_new_robot)

    from .update_robot import on_update_robot
    handler.on('update_robot', on_update_robot)

    from .delete_robot import on_delete_robot
    handler.on('delete_robot', on_delete_robot)

    from .member_visible import on_member_visible
    handler.on('member_visible', on_member_visible)

    from .member_invisible import on_member_invisible
    handler.on('member_invisible', on_member_invisible)

    from .update_file import on_update_file
    handler.on('update_file', on_update_file)

    from .delete_file import on_delete_file
    handler.on('delete_file', on_delete_file)

    from .new_channel_member import on_new_channel_member
    handler.on('new_channel_member', on_new_channel_member)

    from .delete_channel_member import on_delete_channel_member
    handler.on('delete_channel_member', on_delete_channel_member)

    return handler
