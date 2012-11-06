# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Menu(db.Model):
    foods = db.StringListProperty()
    stars = db.IntegerProperty()
    year = db.IntegerProperty()
    month = db.IntegerProperty()
    day = db.IntegerProperty()

    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])


