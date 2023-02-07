import openpyxl
from openpyxl import Workbook
data1=openpyxl.load_workbook('../data/merge.xlsx')
print(data1.get_sheet_names())
active_sheet=data1.active
print(active_sheet)