from openpyxl import load_workbook 
import string
filename = 'words.xlsx'
wb = load_workbook(filename = filename)
range_names = 'Sheet1'
sheet_ranges = wb[range_names]
for column in range(1, 233):
    for row in string.ascii_lowercase[:3]:
        print(sheet_ranges[row+str(column)].value)
print('Gut gemacht!')