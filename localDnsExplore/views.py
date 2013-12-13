from flask import *
from models import *
from localDnsExplore import app
import default_settings


@app.route("/", methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/monkey", methods=['GET','POST'])
def monkey():
  monkeys = Monkey.query.all()
  return render_template('monkey/index.html', monkeys = monkeys)

#@app.before_request
#def before_request():
#  print "before request"
