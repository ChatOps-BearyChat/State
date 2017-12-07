# -*- coding: utf-8 -*-


def on_update_robot(store, message):
    data = message['data']
    robot_id = data['id']
    robot = store.get_robot_by_id(robot_id)
    robot.update(**data)
