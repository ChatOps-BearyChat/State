# -*- coding: utf-8 -*-

from bcmm.logging import logger
from bcmm.model.user import User
from bcmm.model.channel import Channel
from bcmm.model.file import File
from bcmm.model.robot import Robot


class Store(object):

    def __init__(self, **kwargs):
        self.team = None
        self.users = dict()
        self.channels = dict()
        self.files = dict()
        self.robots = dict()

    def set_team(self, team, _force=False):
        if self.team is not None and not _force:
            logger.warning('Failed to set team, since team is not None and'
                           '`_force` is not set')

        self.team = team

    def set_users_directly(self, users, _force=False):
        if len(self.users) > 0 and not _force:
            logger.warning('Failed to set users, since users is not empty and'
                           '`_force` is not set')
            return

        if not isinstance(users, dict):
            logger.error('Failed to set users, since users is not '
                         'an instance of dict')
            return

        self.users = users

    def set_channels_directly(self, channels, _force=False):
        if len(self.channels) > 0 and not _force:
            logger.warning('Failed to set channels, since channels is not '
                           'empty and `_force` is not set')

        if not isinstance(channels, dict):
            logger.error('Failed to set channels, since channels is not '
                         'an instance of dict')
            return

        self.channels = channels

    def set_files_directly(self, files, _force=False):
        if len(self.files) > 0 and not _force:
            logger.warning('Failed to set files, since files is not '
                           'empty and `_force` is not set')

        if not isinstance(files, dict):
            logger.error('Failed to set files, since files is not '
                         'an instance of dict')
            return

        self.files = files

    def set_robots_directly(self, robots, _force=False):
        if len(self.robots) > 0 and not _force:
            logger.warning('Failed to set robots, since robots is not '
                           'empty and `_force` is not set')

        if not isinstance(robots, dict):
            logger.error('Failed to set files, since files is not '
                         'an instance of dict')
            return

        self.robots = robots

    def add_user(self, user):
        if not isinstance(user, User):
            logger.error('Failed to add user, since user is not '
                         'an instance of `bcmm.model.User`')
            return

        self.users[user.pk] = user

    def add_channel(self, channel):
        if not isinstance(channel, Channel):
            logger.error('Failed to add user, since channel is not '
                         'an instance of `bcmm.model.Channel`')
            return

        self.channels[channel.pk] = channel

    def add_file(self, file_):
        if not isinstance(file_, File):
            logger.error('Failed to add user, since file is not '
                         'an instance of `bcmm.model.File`')
            return

        self.files[file_.pk] = file_

    def add_robot(self, robot):
        if not isinstance(robot, Robot):
            logger.error('Failed to add robot, since robot is not '
                         'an instance of `bcmm.model.Robot`')
            return

        self.robots[robot.pk] = robot

    def _get_user_by_pk(self, pk):
        return self.users.get(pk)

    def get_team(self):
        return self.team

    def get_user_by_id(self, id_):
        return self._get_user_by_pk(id_)

    def _get_channel_by_pk(self, pk):
        return self.channels.get(pk)

    def get_channel_by_id(self, id_):
        return self._get_channel_by_pk(id_)

    def _get_file_by_pk(self, pk):
        return self.files.get(pk)

    def get_file_by_id(self, id_):
        return self._get_file_by_pk(id_)

    def _get_robot_by_pk(self, pk):
        return self.robots.get(pk)

    def get_robot_by_id(self, id_):
        return self._get_robot_by_pk(id_)

    def remove_user(self, user_id):
        del self.users[user_id]

    def remove_channel(self, channel_id):
        del self.channels[channel_id]

    def remove_robot(self, robot_id):
        del self.robots[robot_id]

    def remove_file(self, file_id):
        del self.files[file_id]
