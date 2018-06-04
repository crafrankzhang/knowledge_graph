# -*- coding: utf-8 -*- 


from flask import Flask

app = Flask("KG_API")
app.config.from_object("server.config")

import views
import models
