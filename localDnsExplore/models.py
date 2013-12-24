import commands
import random
import string

class Monkey():

  def __init__(self, hostname, domain, ip, commit_time):
    self.hostname = hostname
    self.domain   = domain
    self.edge_server_ip = ""
    self.client_ip = ip
    self.commit_time = commit_time

  def save(self):
    cmd      = "awk '/" + self.domain[:-5] + "/{print}'" + " /var/named/query.log|sed -n '$p'"
    dnsStrs  = commands.getoutput(cmd)
    cname = self.hostname
    iscc = lambda strs:strs.endswith("ccgslb.net") or strs.endswith("ccgslb.com") or strs.endswith("chinacache.net") or strs.endswith("ccgslb.com.cn")
    try:
      self.local_dns = dnsStrs.split()[6].split("#")[0]
      if(self.hostname):
        if not iscc(self.hostname):
          cmd = "dig " + self.hostname
          res = commands.getoutput(cmd)
          for ll in res.split("\n"):
            strs = ll.split()
            if len(strs)==5 and not strs[0].startswith(";") and strs[3]=="CNAME":
              cname = strs[4][:-1]

        if iscc(cname):
          ccdig = "ccdig.sh" + " 202.106.196.115 " + cname + " S " +self.local_dns
          res   = commands.getoutput(ccdig)
          for line in res.split("\n"):
            strip = line.split()
            if len(strip)>0 and strip[0]=='"RR:A':
              self.edge_server_ip += (strip[2][:-1] + " ")
    except Exception, e:
      print e
    finally:
      print "end process"
