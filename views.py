
import os
import json
import xlrd
import webapp2
from google.appengine.api import memcache



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("PositaGrill")

class UploadHandler(webapp2.RequestHandler):
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
        worksheet = workbook.sheet_by_name('Sheet2')

        num_rows = worksheet.nrows - 1
        current_row = -1

        while current_row < num_rows:
            current_row += 1
            row = worksheet.row(current_row)
            self.response.write(row)


class MenuHandler(webapp2.RequestHandler):
    def get(self, day, month, year):
        self.response.out.write(str(year))

