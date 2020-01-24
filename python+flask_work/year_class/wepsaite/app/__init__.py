from flask import Flask
import os

app = Flask(__name__)
app.config['Data_PATH']

from app import routes