#!/usr/bin/env python

import gspread 
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name('capstoneuserdata-bac01be34e74.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('UserInfo').sheet1

##print(wks.get_all_records())

x = wks.find('sjasthi').row
print(wks.row_values(x))