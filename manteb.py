import cgi
import os
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Greeting(db.Model):
  image = db.Blob

class MainPage(webapp.RequestHandler):
  def get(self):
    template_values = {
      'greetings': "From Template",
    }
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path,template_values))

  def post(self):
    template_values = {
      'greetings': "From Template",
    }
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path,template_values))

class CallbackHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
      'greetings': "From Template",
    }
    path = os.path.join(os.path.dirname(__file__), 'callback_handler.html')
    self.response.out.write(template.render(path,template_values))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/post', MainPage),
                                      ('/callback', CallbackHandler)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()