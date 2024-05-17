import pandas as pd
from openpyxl import load_workbook


workbook = pd.read_excel('mac.xlsx')
workbookWrite = load_workbook(filename='mac.xlsx')
sheet = workbookWrite.active

serialNumber = 'used'

print(workbook['MAC'].size)
found = -1
for i in range(workbook['MAC'].size):
    if(workbook['Serial Number (used)'].isnull().iloc[i]):
        print('next available: ', workbook['MAC'].iloc[i])
        sheet["B" + str(i+2)] = serialNumber + str(i)
        found = i
        print('found')
        break
    

workbookWrite.save(filename='mac.xlsx')
print(workbook['MAC'].iloc[found])
