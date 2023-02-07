import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook('../data/demo_workbook_write.xlsx')
sheet=wb.active
sheet['F1'].value='=SUM(A:E)'
wb.save('../data/demo_workbook_write1.xlsx')
