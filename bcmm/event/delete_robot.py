# -*- coding: utf-8 -*-


def on_delete_robot(store, message):
    data = message['data']
    robot_id = data['id']
    store.delete_robot(robot_id)
