from flask import *
a = 1
def test_db():
  print "DB is ok"

app = Flask(__name__)
app.config.from_object("localDnsExplore")
app.config["DEBUG"]=True
