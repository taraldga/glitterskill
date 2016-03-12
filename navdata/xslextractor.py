import xlrd
import os
from bs4 import BeautifulSoup
import datetime

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
	print "sdasdsadsa asdsad asd as dsa "
	workbook = xlrd.open_workbook(path)
	sheet = workbook.sheet_by_index(0)
	n = sheet.ncols
	for row in range(sheet.nrows-10000):
		ID = sheet.cell_value(row,1)
		ISCO = sheet.cell_value(row,9)
		beskrivelse = clean_tags(sheet.cell_value(row,6))
		beskrivelse2 = sheet.cell_value(row,7)
		beskrivelse2 = clean_tags(beskrivelse2)
		Arbeidssted = sheet.cell_value(row,11)
		date = make_date(sheet.cell_value(row,2))
		print date

def main():
	traverse_notebook('LS.xlsx')  #Edit this line to match the path of the workbook.

main()






