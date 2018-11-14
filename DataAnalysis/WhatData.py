import csv
import sys
import xlrd

def opencsv():
    filename = "./BUG.csv"
    data = []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            data = [row for row in reader]
    except csv.Error as e:
        sys.exit(-1)
    if header:
        print(header)
        print('=========')
    for datarow in data:
        print(data)

def openExcel():
    filename = './asdf.xlsx'
    wb = xlrd.open_workbook(filename=filename)
    worksheet = wb.sheet_by_name('Sheet1')
    dataSet = []
    for i in range(ws.nrows):
         row = worksheet.row(i)
        for j in range(0, worksheet.ncols):
            print(worksheet.cell(i.j).value, "\t", end="")


if __name__ == '__main__':
    opencsv()