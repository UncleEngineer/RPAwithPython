from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import subprocess

excelfile = Workbook()
sheet = excelfile.active

data = [['ชนิดต้นไม้','สีใบ','ความสูง'],
        ['ต้นมะม่วง','สีเขียวเข้ม',5],
        ['ต้นกล้วย','เขียวอ่อน',3],
        ['ต้นซารุกะ','สีชมพู',4]]

for d in data:
    sheet.append(d)

values = Reference(sheet,min_col=3,max_col=3, min_row=2,max_row=4)
chart = BarChart()
chart.title = 'ความสูงต้นไม้'
chart.y_axis.title = 'ความสูง'
chart.x_axis.title = 'ชนิดต้นไม้'
chart.legend = None

chart.add_data(values)
sheet.add_chart(chart,'E5')

cat = Reference(sheet, min_col=1,max_col=1, min_row=2, max_row=4)
chart.set_categories(cat)

excelfile.save('basic-excel.xlsx')
#open file
subprocess.Popen('basic-excel.xlsx',shell=True)