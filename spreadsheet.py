import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
client = gspread.authorize(creds)

#fine a workbook and use it name, done forget to share the work book with the
#client email address in order to have access to it.
sheet = client.open("Python with excel").sheet1

pp = pprint.PrettyPrinter()

#this will print all records
result = sheet.get_all_records()

#this will print row value for a particular row
result1 = sheet.row_values(5)

#this will print coloum value for a particular coloum
result2 = sheet.col_values(4)

#this will print cell value for a particular cell
result3 = sheet.cell(5,5).value
pp.pprint(result3)

#this will change the result of a particular cell
sheet.update_cell(5, 5, 'MALE')
result4 = sheet.cell(5, 5).value

pp.pprint(result4)
