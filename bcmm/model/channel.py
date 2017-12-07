# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bcmm.model.base import Model


class Channel(Model):

    def __init__(self, **kwargs):
        self.pk = kwargs['id']

        self.update(_replace=True, **kwargs)

        super(Channel, self).__init__()

    def update(self, **kwargs):
        _replace = kwargs.get('_replace', False)

        fields = ('id', 'name', 'topic', 'description', 'type', 'vchannel_id')

        for field in fields:
            v = kwargs.get(field)
            if v or _replace:
                setattr(self, field, v)

        member_ids = map(lambda x: x['uid'], kwargs.get('members', []))
        self.member_ids = set(member_ids)

        if _replace:
            self.owner_id = kwargs.get('uid')
            self.is_general = kwargs.get('general')
            self.is_inactive = kwargs.get('inactive')
        else:
            if 'uid' in kwargs:
                self.owner_id = kwargs.get('uid')

            if 'general' in kwargs:
                self.is_general = kwargs.get('general')

    def archive(self):
        self.is_inactive = True

    def unarchive(self):
        self.is_inactive = False

    def add_member(self, uid):
        self.member_ids.add(uid)

    def remove_member(self, uid):
        self.member_ids.remove(uid)
