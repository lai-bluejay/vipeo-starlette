#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/Users/charleslai/PycharmProjects/ivideo-flask.forms.py was created on 2019/03/12.
file in :relativeFile
Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""
import requests
import json
from wtforms import Form, TextField, StringField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.compat import iteritems

def make_choice(api_name):
    with open('assets/analyze.json', ) as fi:
        api = json.load(fi)
    return [(a['url'], a['name']) for a in api[api_name]]


sentinel = object()
SUBMIT_VERBS = frozenset({'DELETE', 'PATCH', 'POST', 'PUT'})

class VipListForm(Form):
    parser = SelectField(u'解析线路', validators=[validators.DataRequired()], choices=make_choice('list'), coerce=str)
    url = StringField(u'请输入视频地址', validators=[validators.DataRequired()])
    submit = SubmitField(u'解析')


    
    # async def is_submitted(self):
    #     """Consider the form submitted if there is an active request and
    #     the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    #     """

    #     return _is_submitted()