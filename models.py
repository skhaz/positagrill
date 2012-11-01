# -*- coding: utf-8 -*-

from google.appengine.ext import db


class Menu(db.Model):
    foods = db.StringListProperty()
    date = db.DateProperty()
    stars = db.IntegerProperty()

