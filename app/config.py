import os
from dotenv import load_dotenv

load_dotenv('.thermal_back_env')

class Config(object):
    # FLASK_ENVIRON gets set in run_debug.sh for development
    # and in systemd for production
    FLASK_APP = os.environ.get('FLASK_APP') or 'web_server.py'
    DB = os.environ.get('DB') or './thermal_printer_db.sqlite'
    SECRET_KEY = os.environ.get('SESSION_SECRET') or "abc123"
