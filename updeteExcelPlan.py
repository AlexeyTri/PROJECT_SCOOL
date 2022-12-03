import os
import openpyxl
from openpyxl import load_workbook


# book = openpyxl.open(r'C:\Users\Alexey.Litovchenko\OneDrive - Colliers International\Desktop\Сводный план-график 2022 11 27.xlsx', read_only=True)
#
# sheet = book.active
# print(sheet['C2'].value)


# os.path.dirname()
# путь к файлу
# file_dir = os.path.dirname('Сводный план-график 2022 11 27.xlsx')
dir = os.path.dirname('Сводный план-график 2022 11 27.xlsx')
# print(os.path.abspath(os.path.join(os.path.dirname('Сводный план-график 2022 11 27') + 'Сводный план-график 2022 11 27.xlsx')))
# print(os.path.dirname('Сводный план-график 2022 11 27.xlsx'))
print(os.path.join( os.getcwd(), 'Сводный план-график 2022 11 27.xlsx' ))
# print(r'C:\Users\Alexey.Litovchenko\OneDrive - Colliers International\Desktop')