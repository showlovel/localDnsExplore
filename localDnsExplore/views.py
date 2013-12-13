from flask import *
from models import *
from localDnsExplore import app

@app.route("/", methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/monkey", methods=['GET'])
def monkey():
  return render_template('index.html')
