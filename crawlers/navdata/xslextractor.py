 # -*- coding: utf-8 -*-
import xlrd
import os
from bs4 import BeautifulSoup
import datetime
import sqlite3

def clean_tags(str_with_tags):
	soup = BeautifulSoup(str_with_tags, "lxml")
	cleaned = soup.getText()
	return cleaned

def make_date(date):
	if(type(date) is float):
		strdate = str(date)
		year = int(strdate[0:4])
		month = int(strdate[4:6])
		date = datetime.datetime(year,month,1)
		return date

def traverse_notebook(path):
	conn = sqlite3.connect('database.db')
	conn.text_factory = str
	cursor = conn.cursor()

	workbook = xlrd.open_workbook(path)
	sheet = workbook.sheet_by_index(0)
	n = sheet.ncols
	for row in range(4, sheet.nrows-10000):
		id = int(sheet.cell_value(row,1))
		title = sheet.cell_value(row,4)
		isco = sheet.cell_value(row,9)
		description = clean_tags(sheet.cell_value(row,6))
		description2 = clean_tags(sheet.cell_value(row,7))
		branch = sheet.cell_value(row,11)
		region = sheet.cell_value(row,15)[3:]
		date = make_date(sheet.cell_value(row,2))
		source = "nav"

		print id

		if (branch == 'Ingeniør- og ikt-fag'.decode("utf-8")) and ('utvikler' in description):
			job_query = 'INSERT INTO  job(id, title, description, region, branch, source, date)' + 'VALUES (?, ?, ?, ?, ?, ?, ?);'
			params = (id, title, description, region, branch, source, date)
			#cursor.execute(job_query, params)

  # conn.commit()
  # conn.close()


def main():
	traverse_notebook('LS.xlsx')  #Edit this line to match the path of the workbook.

main()






