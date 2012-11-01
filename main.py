#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from views import MainHandler, UploadHandler, MenuHandler


app = webapp2.WSGIApplication([
        ('/', MainHandler),
        ('/upload', UploadHandler),
        (r'/menu/(\d+)/(\d+)/(\d+)/?$', MenuHandler),
    ], debug=True)

