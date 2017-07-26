import xlrd

data = xlrd.open_workbook('liu.xls')

table = data.sheet_by_name(u'Sheet1')

table.row_values(0)
