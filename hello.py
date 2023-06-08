from openpyxl.workbook import Workbook
from openpyxl import load_workbook

#create a workbbok object
#wb = Workbook()



#load existing spreadsheet
wb = load_workbook('hello.xlsx')

#create an active worksheet
ws = wb.active

#print something from the spreadsheet
print("This is the result")
print(ws["A2"])
print(ws["A2"].value)
print(f'{ws["A2"].value}: {ws["B2"].value}')