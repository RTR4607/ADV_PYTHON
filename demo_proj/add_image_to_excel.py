from openpyxl import load_workbook
from openpyxl.drawing.image import Image
wb=load_workbook(filename='../data/demo_workbook_write.xlsx')
sheet=wb.active
logo=Image('../data/logo.jfif')
logo.height=150
logo.width=150
sheet.add_image(logo,'D10')
wb.save(filename='../data/demo_workbook_write2.xlsx')