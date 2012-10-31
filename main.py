#!/usr/bin/env python

import webapp2
from views import MainHandler, UploadHandler, MenuHandler


app = webapp2.WSGIApplication([
        ('/', MainHandler),
        ('/upload', UploadHandler),
        (r'/menu/(\d+)/(\d+)/(\d+)/?$', MenuHandler),
    ], debug=True)

