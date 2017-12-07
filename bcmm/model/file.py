# -*- coding: utf-8 -*-

from bcmm.model.base import Model


class File(Model):

    def __init__(self, **kwargs):
        self.pk = kwargs['id']

        fields = ('id', 'name', 'title', 'url', 'mime', 'description')

        for field in fields:
            setattr(self, field, kwargs.get(field))

        self.owner_id = kwargs.get('uid')
