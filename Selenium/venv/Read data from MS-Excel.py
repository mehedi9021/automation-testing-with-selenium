import openpyxl

path = "C:\\Users\\User\\PycharmProjects\\Selenium\\venv\weather.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active #for single sheet
#sheet = workbook.get_sheet_by_name("sheet name") #for multiple sheet

rows = sheet.max_row
col = sheet.max_column

print(rows)
print(col)

for r in range (1, rows+1):
    for c in range (1, col+1):
        print(sheet.cell(row = r, column = c).value, end = "    ")

    print()