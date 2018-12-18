#! /usr/bin/env bash

export FLASK_ENVIRON=production
gunicorn --bind 0.0.0.0:5000 wsgi:app