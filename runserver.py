from gevent.wsgi import WSGIServer
from localDnsExplore import app
http_server =  WSGIServer(('', 5000), app)
http_server.serve_forever()
#app.run(host="0.0.0.0")
