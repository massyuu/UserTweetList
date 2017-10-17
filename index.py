#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./template/', encoding='utf8'))

def index(user_name, tweets):
    tpl = env.get_template('index.html')
    return tpl.render(user_name=user_name , tweets = tweets)
