from flask import *

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

if __name__=="__main__":
  app.run(debug = True)
