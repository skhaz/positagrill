#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from views import MainHandler, UploadHandler, MonthlyMenuHandler, DailyMenuHandler, PollHandler

app = webapp2.WSGIApplication([
        ('/', MainHandler),
        ('/upload', UploadHandler),
        (r'/menu/(\d+)/(\d+)/?$', MonthlyMenuHandler),
        (r'/menu/(\d+)/(\d+)/(\d+)/?$', DailyMenuHandler),
        (r'/poll/(\d+)/(\d+)/(\d+)/?$', PollHandler),
    ], debug=True)

