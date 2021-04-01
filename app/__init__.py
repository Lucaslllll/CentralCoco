from flask import Flask

app = Flask(__name__)

from app.controllers import default # normal esse tipo de importação no flask