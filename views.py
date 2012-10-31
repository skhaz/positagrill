
import os
import json
import webapp2
from google.appengine.api import memcache



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("PositaGrill")

class UploadHandler(webapp2.RequestHandler):
    pass

class MenuHandler(webapp2.RequestHandler):
    def get(self, day, month, year):
        self.response.out.write(str(year))

