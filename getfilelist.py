import os

pythonfile_path = os.getcwd()
excel_folder = os.path.join(pythonfile_path,'excelfile')
file_list = os.listdir(excel_folder)

for f in file_list:
    print(f)