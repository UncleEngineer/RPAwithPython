from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import subprocess
import random
import os

pythonfile_folder = os.getcwd() #current directory
excel_folder = os.path.join(pythonfile_folder,'excelfile')

for i in range(1,101):
    excelfile = Workbook()
    sheet = excelfile.active

    data = [['ชนิดต้นไม้','สีใบ','ความสูง'],
            ['ต้นมะม่วง','สีเขียวเข้ม',random.randint(3,30)],
            ['ต้นกล้วย','เขียวอ่อน',random.randint(3,30)],
            ['ต้นซารุกะ','สีชมพู',random.randint(3,30)]]

    for d in data:
        sheet.append(d)

    excel_name = 'data-no-graph-{}.xlsx'.format(i)
    excel_path = os.path.join(excel_folder, excel_name)
    excelfile.save(excel_path)
    #open file
    # subprocess.Popen('basic-excel.xlsx',shell=True)