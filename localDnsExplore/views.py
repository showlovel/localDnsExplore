#encoding:utf-8
from flask import *
from models import *
from localDnsExplore import app
import default_settings
import utils


# 问题提交页面
@app.route("/", methods=['GET'])
def index():
  #utils.mailTo("","")
  return render_template('index.html')

# 查看已经提交的问题
@app.route("/monkeys/", methods=['GET'])
@app.route("/monkeys",  methods=['GET'])
def monkeys():
  monkeys = Monkey.query.all()
  return render_template('monkey/index.html', monkeys = monkeys)

# 网民提交问题·
@app.route("/monkey", methods=['POST'])
def monkey():
  if request.method=='POST':
    name        = request.form['name']
    phone       = request.form['phone']
    email       = request.form['email']
    company     = request.form['company']
    url         = request.form['url']
    description = request.form['description']
    return render_template('index.html')
  else:
    pass

@app.route("/auto_detect")
@app.route("/auto_detect/<hostname>")
def auto_detect():
  pass

#@app.before_request
#def before_request():
#  print "before request"
