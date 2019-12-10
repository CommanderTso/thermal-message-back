#!./venv/bin/python

from flask_bcrypt import generate_password_hash, check_password_hash
import sys

print("New password hash: " + generate_password_hash(sys.argv[1]).decode('UTF-8'))