# -*- coding: utf-8 -*-

from bcmm.model.user import User


def test_team_model():
    data = {
        "inactive": True,
        "role": "normal",
        "read_ts": 1512124446426,
        "email": "foobar@example.com",
        "star_id": None,
        "presence": "online",
        "latest_ts": 1494822684426,
        "updated": "2017-05-17T07:36:19.000+0000",
        "name": "foobar",
        "index_symbol": "a",
        "type": "normal",
        "created": "2016-11-01T03:56:03.000+0000",
        "vchannel_id": "=dVNX4I2",
        "email_verified": True,
        "mobile_verified": True,
        "hidden": False,
        "id": "=bwKBg",
        "position": "Position",
        "team_id": "=bw52O",
        "full_name": "Foo Bar",
        "mobile": "+8613800138000",
        "avatar_url": "https://static.beary.chat/imGA4ux",
        "conn": "connected",
    }

    user = User(**data)
    assert user.id == '=bwKBg'
    assert user.name == 'foobar'
    assert user.full_name == 'Foo Bar'
    assert user.avatar_url == 'https://static.beary.chat/imGA4ux'
    assert user.position == 'Position'
    assert user.email == 'foobar@example.com'
    assert user.email_verified is True
    assert user.mobile == '+8613800138000'
    assert user.mobile_verified is True
    assert user.type == 'normal'
    assert user.vchannel_id == '=dVNX4I2'
    assert user.role == 'normal'
    assert user.is_connected is True
