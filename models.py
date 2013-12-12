from sqlalchemy import *
import os

class Problem:
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
