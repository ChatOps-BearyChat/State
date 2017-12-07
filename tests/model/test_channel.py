# -*- coding: utf-8 -*-

from bcmm.model.channel import Channel


def test_channel_model():
    data = {
      "inactive": False,
      "description": "channel description",
      "deleted": None,
      "read_ts": 1512051249545,
      "star_id": None,
      "private": False,
      "general": False,
      "latest_ts": 1512051249545,
      "ann_read_ts": 0,
      "updated": "2015-05-21T03:28:01.000+0000",
      "uid": "=bw52O",
      "name": "ChannelName",
      "is_member": True,
      "index_symbol": "b",
      "pin_count": 0,
      "type": "normal",
      "created": "2014-09-02T02:45:12.000+0000",
      "topic": "Channel Topic",
      "member_count": 10,
      "vchannel_id": "=bw52S",
      "preference": {
        "sound": True,
        "desktop_notification": "no",
        "desktop_robot_notification": True,
        "notification": "no",
        "robot_notification": True,
        "mobile_notification_mute": False
      },
      "id": "=bw52S",
      "team_id": "=bw52O",
      "members": [
        {
          "uid": "=bw52S"
        },
        {
          "uid": "=bw53D"
        },
        {
          "uid": "=bw9IS"
        },
        {
          "uid": "=bwEVF"
        },
        {
          "uid": "=bwJzh"
        },
        {
          "uid": "=bwLlk"
        },
        {
          "uid": "=bwL3z"
        },
        {
          "uid": "=bwMHV"
        },
        {
          "uid": "=bwO6w"
        },
        {
          "uid": "=bwSfi"
        }
      ],
      "unread_count": 0,
      "mention_count": 0
    }

    channel = Channel(**data)

    assert channel.id == '=bw52S'
    assert channel.name == 'ChannelName'
    assert channel.topic == 'Channel Topic'
    assert channel.description == 'channel description'
    assert channel.type == 'normal'
    assert channel.vchannel_id == '=bw52S'
    assert channel.owner_id == '=bw52O'
    assert channel.is_general is False
    assert channel.is_inactive is False
