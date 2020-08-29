import openpyxl
from openpyxl import formula

wb = openpyxl.Workbook()
act_sheet = wb.active
act_sheet.title = "Fifty"

for i in range (41,51):
    act_sheet.append([i])

act_sheet.move_range("A1:A10",cols=1)

for i in range (31,41):
    act_sheet.append([i])

wb.save("extra_credit.xlsx")

