
from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
wb=Workbook()
sheet=wb.active
sales=[['year','sales'],
       [2010,12000],
       [2011,12500],
       [2012,13000],
       [2013,13500],
       [2014,14000],
       [2015,14500]
       ]
chart=LineChart()
for row in sales:
    sheet.append(row)
data=Reference(worksheet=sheet,min_row=1,max_row=7,min_col=1,max_col=2)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,'E2')
wb.save('../data/linechart.xlsx')
