#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

# Twitter API の設定
customer_key = 'XXXXX'
customer_secret = 'XXXXX'
access_token = 'XXXXX'
access_token_secret = 'XXXXX'
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

def getUserTimeLine(user_name, count):
    # parameter の設定
    params = {
        "screen_name":user_name
        ,"count":count
        ,"include_rts":"false"
        ,"exclude_replies":"false"
        ,"trim_user":"false"
    }

    # OAuth で GET
    twitter = OAuth1Session(customer_key, customer_secret, access_token, access_token_secret)
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        return json.loads(req.text)
    else:
        # エラーの場合
        return ""