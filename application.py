import configparser
from flask import Flask

app = Flask(__name__)

config = configparser.ConfigParser(allow_no_value=True)
config.optionxform = str
config.read_file(open('configs/settings.cfg', 'r'))
for key in config['DEFAULT']:
    app.config[key] = config['DEFAULT'][key]
