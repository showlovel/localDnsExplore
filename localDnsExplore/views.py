from flask import *
from models import *
from localDnsExplore import app
import default_settings


@app.route("/", methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/monkey", methods=['GET'])
def monkey():
  return render_template('index.html')

@app.before_request
def before_request():
  print "before request"
