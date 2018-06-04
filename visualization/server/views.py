# -*- coding: utf-8 -*-


import os
import time
from functools import wraps

from flask import request,redirect,session,g,Response,render_template

from itsdangerous import JSONWebSignatureSerializer as JWT
from flask_httpauth import HTTPTokenAuth
from schema import Schema, And, Use, Optional, SchemaError

from server import app
from server.errors import *
from server.logger import *
from server import models


logger = config_logger('SERVER.VIEWS', 'INFO', 'server.log')

# auth = HTTPTokenAuth('Bearer')

# ISFORMAT="%Y%m%d%H%M%S"

conn, cursor = models.init()

mydata = ""

@app.route("/api/v1", methods=["GET"])
def parse():
	global mydata
	req = request.args
	# .args.get('username')
	if "entity" in req:
		entity_code = req["entity"]
		mydata = models.execute(conn, cursor, ("entity", entity_code))
	elif "pers" in req:
		name = req["pers"]
		mydata = models.execute(conn, cursor, ("pers", name))		
	# return {"resultmsg":"OK","resultno":ERROR_OK},200
	return render_template('index.html')





@app.route("/api/data")
def data():
	return mydata

