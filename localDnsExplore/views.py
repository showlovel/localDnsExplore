#encoding:utf-8
from flask import *
from models import *
from localDnsExplore import app
from localDnsExplore.database import db_session
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
    monkey             = Monkey()
    monkey.name        = request.form['name']
    monkey.phone       = request.form['phone']
    monkey.email       = request.form['email']
    monkey.company     = request.form['company']
    monkey.url         = request.form['url']
    monkey.description = request.form['description']
    monkey.save()
    monkey.version  = 1
    db_session.add(monkey)
    db_session.commit()
    return redirect(url_for('index'))
  else:
    pass

@app.route("/auto_detect")
@app.route("/auto_detect/<hostname>")
def auto_detect():
  pass

#@app.before_request
#def before_request():
#  print "before request"
