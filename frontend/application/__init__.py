from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.static_folder = "static"
Bootstrap(app)

from application import routes