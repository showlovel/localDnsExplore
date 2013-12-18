#encoding:utf-8
from flask import Flask
from flask.ext.mail import Message
from flask.ext.mail import Mail
from localDnsExplore import app

def mailTo(admins, monkey):
  admins = ['shengyu.yang@chinacache.com']
  mail = Mail(app)
  msg  = Message("test mail send", sender=admins[0], recipients=admins)
  html = "<html><body>" + "网民姓名:"  + "monkey.name<br/>" +"公司:"+ "monkey.company <br/>" + "电话:"+ "monkey.phone<br/>" +"Email:"+ "monkey.email<br/>" + "Url:"+ "monkey.url<br/>" + "客户端ip:"  + "monkey.edge_server_ip<br/>"+"LocalDns:"  + "monkey.local_dns<br/>"+"问题描述:"  + "monkey.description<br/>"+"解析时间:"  + "monkey.commit_time<br/>"+ "</body></html>"
  msg.html = html
  mail.send(msg)
