# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bcmm.model.base import Model


class Robot(Model):

    def __init__(self, **kwargs):
        self.pk = kwargs['id']

        self.update(_replace=True, **kwargs)

        super(Robot, self).__init__()

    def update(self, **kwargs):
        _replace = kwargs.get('_replace', False)
        fields = ('id', 'name', 'target_vchannel_id', 'inactive')
        for field in fields:
            v = kwargs.get(fields)
            if v or _replace:
                setattr(self, field, v)
