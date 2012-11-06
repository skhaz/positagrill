# -*- coding: utf-8 -*-
import os
import json
import xlrd
import json
import webapp2
from datetime import datetime
from models import Menu
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import memcache

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('PositaGrill')

class UploadHandler(webapp2.RequestHandler):
    START_OFFSET = 3
    ROW_OFFSET   = 12
    SHEET_NAME = 'Sheet2'

    def get(self):
        self.response.write('<html><body>')
        self.response.write('<form method="post" action="/upload" enctype="multipart/form-data">')
        self.response.write('<input type="file" name="file" />')
        self.response.write('<input type="submit" value="upload" />')
        self.response.write('</form>')
        self.response.write('</body></hmtl>')

    def post(self):
        upload = self.request.get('file')

        workbook = xlrd.open_workbook(file_contents=upload)
        worksheet = workbook.sheet_by_name(self.SHEET_NAME)
        rows = worksheet.nrows - 1
        columns = worksheet.ncols - 1
        current_column = 0

        while current_column < columns - 1:
            current_column += 1
            current_row = self.START_OFFSET
            while current_row < rows:
                foods = []
                date = None

                for row in xrange(current_row, current_row + self.ROW_OFFSET):
                    cell_type = worksheet.cell_type(row, current_column)
                    cell_value = worksheet.cell_value(row, current_column)

                    if cell_type == 3: # datetime
                        date = datetime(*xlrd.xldate_as_tuple(cell_value, workbook.datemode)).date()
                    else:
                        foods.append(cell_value)

                try:
                    menu = Menu()
                    menu.foods = foods
                    menu.day = date.day
                    menu.month = date.month
                    menu.year = date.year
                    menu.save()
                except:
                    pass

                current_row += self.ROW_OFFSET

        self.response.write('Ok')

class MonthlyMenuHandler(webapp2.RequestHandler):
    def get(self, month, year):
        cache_key = 'monthly_{}_{}'.format(month, year)
        result = memcache.get(cache_key)
        if result is None:
            result = self.render(month, year)
            if not memcache.add(key=cache_key, value=result):
                logging.error('Memcache set failed.')
        self.response.out.write(result)

    def render(self, month, year):
        menu = Menu.gql('WHERE month = {} AND year = {}'.format(month, year))
        if not menu:
            return '[]'
        else:
            return json.dumps([m.to_dict() for m in menu])

class DailyMenuHandler(webapp2.RequestHandler):
    def get(self, day, month, year):
        cache_key = 'daily_{}_{}_{}'.format(day, month, year)
        result = memcache.get(cache_key)
        if result is None:
            result = self.render(day, month, year)
            if not memcache.add(key=cache_key, value=result):
                logging.error('Memcache set failed.')
        self.response.out.write(result)

    def render(self, day, month, year):
        menu = Menu.gql('WHERE day = {} AND month = {} AND year = {}'.format(day, month, year))
        if not menu:
            return '[]'
        else:
            return json.dumps([m.to_dict() for m in menu])

