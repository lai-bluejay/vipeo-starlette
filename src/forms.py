from starlette.requests import Request
from starlette.responses import Response
import requests

from wtforms import Form, TextField, StringField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.compat import iteritems

def make_choice(api_name):
    vip_json = "https://iodefog.github.io/text/mviplistmm.json"
    api = requests.get(vip_json).json()
    return [(a['url'], a['name']) for a in api[api_name]]


sentinel = object()
SUBMIT_VERBS = frozenset({'DELETE', 'PATCH', 'POST', 'PUT'})

class VipListForm(Form):
    parser = SelectField('解析线路', validators=[validators.DataRequired()], choices=make_choice('list'), coerce=str)
    url = StringField('视频地址', validators=[validators.DataRequired()])
    submit = SubmitField('解析')


    
    # async def is_submitted(self):
    #     """Consider the form submitted if there is an active request and
    #     the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    #     """

    #     return _is_submitted()