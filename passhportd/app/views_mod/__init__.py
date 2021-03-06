# -*-coding:Utf-8 -*-

# Compatibility 2.7-3.4
from __future__ import absolute_import
from __future__ import unicode_literals

import flask
from app import app


@app.errorhandler(404)
def page_not_found(error):
    return "ERROR: You must fill the requested fields", 404, \
        {"content-type": "text/plain; charset=utf-8"}
