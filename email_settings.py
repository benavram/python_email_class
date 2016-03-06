# -*- coding: utf-8 -*-
"""Email connection settings & template loader
"""
# from jinja2 import Environment, FileSystemLoader
import os

# ENV = os.environ.get('APP_ENV')
UN = '**********'
PW = '**********'
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = '*****@**********.com'
EMAIL_HOST = 'smtp.***********.com'
EMAIL_PORT = 587

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/')
# J2_ENV = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True)
