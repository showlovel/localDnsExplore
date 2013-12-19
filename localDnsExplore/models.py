from sqlalchemy import *
from sqlalchemy.orm import *
from localDnsExplore.database import Base
import commands
import random
import string

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
  commit_time    = Column(Date)

  def __init__(self):
    pass

  def save(self):
    self.domain = "yachuan" + ''.join(random.sample(string.lowercase,8)) + ".term.chinacache.net"
    cmd         = "awk '/" + self.domain + "/ {print} ' /var/named/query.log|sed -n '$p'"

    print "---------"
    print cmd
    print "---------"

    status, res = commands.getstatusoutput(cmd)

    print "---------"
    print status
    print res
    print "---------"

    serverIp    = ""
    cname = self.hostname
    iscc = lambda domain:domain.endswith("ccgslb.net") or domain.endswith("ccgslb.com") or domain.endswith("chinacache.net")

    try:
      self.local_dns = res.split(" ")[6].split("#")[0]

      if self.hostname and iscc(self.hostname):
        cmd = "dig " + self.hostname
        sts, ccres = commands.getstatusoutput(cmd)

        for ccline in ccres.split("\n"):
          ccstrs = ccline.split()

          if len(ccstrs)==5 and not strs[0].startwidth(";") and strs[3]=="CNAME":
            cname = strs[4][:-2]

            if not iscc(cname):
              ccdigcmd = "/usr/bin/ccdig.sh " + "202.106.196.115" + cname + " S " + self.local_dns
              notccres = commands.getoutput(ccdigcmd)

              for notccline in notccres.split("\n"):
                notccstrs = notccline.split()
                if notccstrs[0]=='"RR:A':
                  serverIp = serverIp + "  " + notccstrs[2][:-2]
                  self.edge_server_ip = serverIp

    except Exception, e:
      print "-----"
      print e
      print "-----"
      raise e
    finally:
      pass

association_table = Table('user_role', Base.metadata,
    Column('user_id', Integer, ForeignKey("user.id")),
    Column('role_id', Integer, ForeignKey("role.id"))
    )

class User(Base):
  __tablename__    = 'user'
  id               = Column(Integer, primary_key=True)
  version          = Column(Integer)
  enabled          = Column(Binary)
  password         = Column(String(255))
  password_expired = Column(String(255))
  username         = Column(String(255))
  children = relationship("Role", secondary=association_table)

  def __init__(self):
    pass

class Role(Base):
  __tablename__ = 'role'
  id        = Column(Integer, primary_key=True)
  version   = Column(Integer)
  authority = Column(String(255))

  def __init__(self):
    pass

