from flask import Flask

app = Flask(__name__)
app.config.from_object("localDnsExplore.default_settings")
import localDnsExplore.views
