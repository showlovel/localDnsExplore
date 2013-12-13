from sqlalchemy import *
from sqlalchemy.orm import *
from localDnsExplore.database import Base
import os

class Monkey(Base):
  __tablename__  = 'monkey'
  id             = Column(Integer, primary_key=True)
  version        = Column(Integer)
  client_ip      = Column(String(255))
  company        = Column(String(255))
  description    = Column(String(255))
  domain         = Column(String(255))
  edge_server_ip = Column(String(255))
  email          = Column(String(255))
  hostname       = Column(String(255))
  local_dns      = Column(String(255))
  name           = Column(String(255), unique=True)
  phone          = Column(String(255))
  url            = Column(String(255))
  regist_id      = Column(String(255))
  commit_time    = Column(String(255))

  def __init__(self, args):
    self.name         = args['name']
    self.phone        = args['phone']
    self.email        = args['email']
    self.url          = args['url']
    self.description  = args['description']
    self.company      = args['company']

  def save(self):
    cmd = "awk '/"+"/ {print} ' /var/named/query.log|sed -n '$p'"
    print cmd

class User:
  pass

class Role:
  pass
