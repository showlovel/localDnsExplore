from flask import Flask
from flask.ext.mail import Message
from flask.ext.mail import Mail
from localDnsExplore import app

def mailTo(name):
  print "send Mail to " + name
  ADMINS = ['shengyu.yang@chinacache.com']
  mail = Mail(app)
  msg  = Message("test mail send", sender=ADMINS[0], recipients=ADMINS)
  msg.html = "<b>Hi </b>" + name
  mail.send(msg)
