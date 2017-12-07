# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bcmm.model.base import Model


class User(Model):

    def __init__(self, **kwargs):
        self.pk = kwargs['id']

        self.update(_replace=True, **kwargs)

        super(User, self).__init__()

    def update(self, **kwargs):
        _replace = kwargs.get('_replace', False)

        fields = ('id', 'name', 'full_name', 'avatar_url', 'position',
                  'email', 'email_verified', 'mobile', 'mobile_verified',
                  'type', 'vchannel_id', 'role')

        for field in fields:
            v = kwargs.get(field)
            if v or _replace:
                setattr(self, field, v)

        if _replace:
            self.is_inactive = kwargs.get('inactive')
            self.is_connected = kwargs.get('conn') == 'connected'
        else:
            if 'inactive' in kwargs:
                self.is_inactive = kwargs.get('inactive')
            if 'conn' in kwargs:
                self.is_connected = kwargs.get('conn') == 'connected'

    def archive(self, **kwargs):
        self.is_inactive = False

    def unarchive(self, **kwargs):
        self.is_inactive = True
