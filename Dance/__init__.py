# -*- coding: UTF-8 -*-

from flask import Flask
import os
from Dance.config import cf
import threading
import sys


templateDir = os.path.join(os.getcwd(), "Dance", "web", "templates")
staticDir = os.path.join(os.getcwd(), "Dance", "web", "static")

app = Flask(__name__, template_folder=templateDir, static_folder=staticDir)

app.config.from_object(cf)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from Dance.web import views



