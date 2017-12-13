# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import logging


def has_handler(logger):
    level = logger.getEffectiveLevel()
    current = logger

    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True

        if not current.propagate:
            break

        current = current.parent

    return False


default_handler = logging.StreamHandler(sys.stderr)
default_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))


def create_logger():
    logger = logging.getLogger("bcmm.logger")

    if logger.level == logging.NOTSET:
        logger.setLevel(logging.DEBUG)

    if not has_handler(logger):
        logger.addHandler(default_handler)

    return logger


logger = create_logger()
