#encoding:utf-8
from flask import *
from models import *
from localDnsExplore import app
import default_settings
import utils
import time

@app.route("/auto_detect")
@app.route("/auto_detect/<hostname>")
def auto_detect():
  hostname = request.args['hostname']
  domain   = "yachuan" + ''.join(random.sample(string.lowercase,18)) + ".term.chinacache.net"
  print domain
  return render_template("info.html", domain=domain, hostname=hostname)

@app.route("/query",  methods=['GET'])
def query():
  hostname = request.args['hostname']
  domain   = request.host
  ip       = request.remote_addr
  now      = time.strftime("%Y-%m-%d %H:%M:%S")
  monkey   = Monkey(hostname, domain, ip, now)
  monkey.save()
  infos = {}
  infos['client']      = monkey.client_ip
  infos['local_dns']   = monkey.local_dns
  infos['edge_server'] = monkey.edge_server_ip
  infos['commit_time'] = monkey.commit_time
  return  jsonify(infos)
