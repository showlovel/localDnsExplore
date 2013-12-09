import os

class Problem:
  def __init_(self):
    pass
    #self.name         = name
    #self.phone        = phone
    #self.email        = email
    #self.url          = url
    #self.description  = description
    #self.clientIp     = clientIp
    #self.localDns     = localDns
    #self.edgeServerIp = edgeServerIp
    #self.hostname     = hostname
    #self.company      = company
    #self.registId     = registId
    #self.domain       = domain

  def save(self):
    cmd = "awk '/", self.domain, "/ {print} ' /var/named/query.log|sed -n '$p'"
    print cmd
