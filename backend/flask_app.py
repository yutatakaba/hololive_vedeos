# -*- coding: utf-8 -*-
"""
配信カレンダーアプリの入り口
"""
from flask import Flask

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
app.config.update(
	JSON_AS_ASCII=True,
	PROPAGATE_EXCEPTIONS=True
)
