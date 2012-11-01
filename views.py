# -*- coding: utf-8 -*-
import os
import json
import datetime
import xlrd
import json
import webapp2
from models import Menu
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import memcache



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("PositaGrill")

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
                        date = datetime.datetime(*xlrd.xldate_as_tuple(cell_value, workbook.datemode)).date()
                    else:
                        foods.append(cell_value)

                menu = Menu()
                menu.foods = foods
                menu.date = date
                menu.save()

                current_row += self.ROW_OFFSET

class MenuHandler(webapp2.RequestHandler):
    def get(self, day, month, year):
        self.response.out.write(json.dumps(Menu.all()))

