#encoding:utf-8
from flask import render_template, request
from models import *
from localDnsExplore import app
import utils
import time

@app.route("/auto_detect", methods=['GET'])
def auto_detect():
  hostname = request.args['hostname']
  app.logger.info("auto_detect:hostname="+hostname)
  domain   = "yachuan" + ''.join(random.sample(string.lowercase,18)) + ".term.chinacache.net"
  return render_template("info.html", domain=domain, hostname=hostname)

@app.route("/query",  methods=['GET'])
def query():
  hostname = request.args['hostname']
  app.logger.info("query:hostname="+hostname)
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
  return  "var $_lanxun_cdn_servers={'client':'"+monkey.client_ip +"', 'local_dns':'" +monkey.local_dns +"', 'edge_server':'"+monkey.edge_server_ip+"', 'commit_time':'" + monkey.commit_time +"'}"
