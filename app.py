#!/usr/bin/python

import re

from functools import wraps
from flask import Flask, render_template, request, send_from_directory, redirect, g, jsonify

from html import *
import search

from handlers_html import *
from handlers_json import *

from logger import *

def debug(str):
  logger.debug(request.remote_addr + ' ' + str)

def info(str):
  logger.info(request.remote_addr + ' ' + str)

class MyFlask(Flask):
  def get_send_file_max_age(self, name):
    if re.search('\.(js|css|png|jpg|ico|woff|ttf|eof|svg)$', name.lower()):
      return 28*24*60*60 # 28 days
    return Flask.get_send_file_max_age(self, name)

# Jinja filters
def byte(a,b):
  return (a>>(8*b)) & 0xFF

def char(a,b):
  return chr(ord(b)+a)

# Route decorators
def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    g.entry = None #Authenticate(request.cookies, request.remote_addr)
    return f(*args, **kwargs)
  return decorated_function

# Flask application
application = MyFlask(__name__)
application.debug = True

application.jinja_env.filters['byte'] = byte
application.jinja_env.filters['char'] = char

# Routes

@application.route("/")
def top():
  return redirect('/index')

@application.route('/what', methods=['GET', 'POST'])
def logged_out_json():
  page = request.path[1:]
  values = dict([(x,'|'.join(request.values.getlist(x))) for x in request.values.keys()])
  json = request.get_json()
  if json: values.update(json)

  info('%s: %s' % (page, values))

  func = globals().get("handle_%s" % page)
  data = func(None, values, request.files)
  info('%s: %s' % (page, data))
  return jsonify(data)

@application.route("/index")
@application.route("/about")
@application.route('/find', methods=['GET', 'POST'])
def logged_out_html():
  page = request.path[1:]
  values = dict([(x,'|'.join(request.values.getlist(x))) for x in request.values.keys()])
  json = request.get_json()
  if json: values.update(json)

  info('%s: %s' % (page, values))

  attrs = html_defaults(request.host,request.user_agent.string)
  attrs.update(values)

  func = globals().get("handle_%s" % page)
  if func: attrs.update(func(None,values))
  html = render_template(page+'.html', **attrs)
  return html

@application.route("/game")
@login_required
def logged_in_html():
  page = request.path[1:]
  values = dict([(x,'|'.join(request.values.getlist(x))) for x in request.values.keys()])
  json = request.get_json()
  if json: values.update(json)

  info('%s: %s' % (page, values))
  #info('%s: id:%d %s' % (page, id, values))

  attrs = html_defaults(request.host,request.user_agent.string)
  attrs.update(values)

  func = globals().get("handle_%s" % page)
  if func: attrs.update(func(g.entry,values))
  return render_template(page+'.html', **attrs)

@application.route("/<path:path>")
def the_rest(path):
  info(path)

  return send_from_directory(application.static_folder, path.encode('utf-8'))

if __name__ == "__main__":
  application.run()
