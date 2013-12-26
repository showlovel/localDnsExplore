import logging
from flask import Flask
from logging.handlers  import RotatingFileHandler

app = Flask(__name__)
file_handler = RotatingFileHandler('log/query.log', 'a', 10*1024*1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.config.from_object("localDnsExplore.default_settings")
import localDnsExplore.views
