from flask import *
from models import *
from localDnsExplore import app
import default_settings
import utils


@app.route("/", methods=['GET'])
def index():
  users = User.query.all()
  print users[0].children[0].authority
  return render_template('index.html')

@app.route("/monkeys", methods=['GET','POST'])
def monkeys():
  monkeys = Monkey.query.all()
  return render_template('monkey/index.html', monkeys = monkeys)

@app.route("/monkey", methods=['GET','POST'])
def monkey():
  monkeys = Monkey.query.all()
  return render_template('monkey/index.html', monkeys = monkeys)

#@app.before_request
#def before_request():
#  print "before request"
