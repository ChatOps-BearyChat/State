# -*- coding: utf-8 -*-

from bcmm.model.team import Team


def test_team_model():
    data = {
        "created": "2014-08-29T07:15:34.000+0000",
        "description": "Description",
        "email_domain": "bearyinnovative.com",
        "id": "=bw52O",
        "inactive": False,
        "logo_url": "https://static.beary.chat/xXpl4M",
        "name": "Beary Innovative",
        "plan": "standard",
        "preference": {
            "prior_name": "fullname"
        },
        "subdomain": "beary",
        "updated": "2017-11-29T07:05:47.000+0000"
    }
    team = Team(**data)

    assert team.name == 'Beary Innovative'
    assert team.subdomain == 'beary'
    assert team.description == 'Description'
    assert team.logo_url == 'https://static.beary.chat/xXpl4M'
    assert team.plan == 'standard'
