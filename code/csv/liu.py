import csv
with open('liu.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
    	print(row[1])

f.close()