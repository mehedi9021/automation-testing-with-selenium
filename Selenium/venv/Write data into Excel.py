import openpyxl

path = "C:\\Users\\User\\PycharmProjects\\Selenium\\venv\write.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range (1, 6):
    for c in range (1, 6):
        sheet.cell(row=r, column=c).value="1"

workbook.save(path)