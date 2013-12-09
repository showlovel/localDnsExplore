from flask import *
from models import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
  return render_template('hello.html',name=name)

@app.route("/bdcreate", methods=['POST'])
def breakdownCreate():
  return render_template('breakdown/new.html',name="Default")

@app.route("/problem", methods=['GET', 'POST', 'DELETE', 'PUT'])
def problem():
  if request.method == "GET":
    print "GET"
    return ""
  elif request.method == "POST":

    name    = request.form['name']
    email   = request.form['email']
    phone   = request.form['phone']
    company = request.form['company']
    url     = request.form['url']
    detail  = request.form['detail']

    p = Problem()
    p.save()

    return "Hello" + name
  elif request.method == "DELETE":
    print "DELETE"
    return ""
  elif request.method == "PUT":
    print "PUT"
    return ""
  else:
    print "OTHER"
    return ""

if __name__=="__main__":
  app.run(debug = True)
