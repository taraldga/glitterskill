import xlrd
import os
from bs4 import BeautifulSoup


def clean_tags(str_with_tags):
	soup = BeautifulSoup(str_with_tags)
	cleaned = soup.getText()
	return cleaned

def make_date(date):
	if(type(date) is float):
		strdate = str(date)
		year = strdate[0:4]
		month = strdate[4:6]
		print month,year




def traverse_notebook(path):
	workbook = xlrd.open_workbook(path)
	sheet = workbook.sheet_by_index(0)
	n = sheet.ncols
	for row in range(sheet.nrows-10000):
		ID =sheet.cell_value(row,1)
		ISCO=sheet.cell_value(row,9)
		beskrivelse=sheet.cell_value(row,6)
		beskrivelse=clean_tags(beskrivelse)
		beskrivelse2=sheet.cell_value(row,7)
		beskrivelse2=clean_tags(beskrivelse2)
		Arbeidssted = sheet.cell_value(row,11)
		Dato=sheet.cell_value(row,2)
		#make_date(Dato)

def main():
	traverse_notebook('C:\Users\Tarald\Documents\EIT\LS.xlsx')  #Edit this line to match the path of the workbook.

main()