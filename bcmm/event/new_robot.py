# -*- coding: utf-8 -*-

from bcmm.model.robot import Robot


def on_new_robot(store, message):
    data = message['data']
    robot = Robot(**data)
    store.add_robot(robot)
