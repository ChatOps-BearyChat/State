# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging


def create_logger():
    logger = logging.getLogger("bcmm.logger")
    return logger


logger = create_logger()
