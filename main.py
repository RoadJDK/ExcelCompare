from itertools import zip_longest
import xlrd

df1 = xlrd.open_workbook(r'data.xls').sheet_by_name('Sheet1')
df2 = xlrd.open_workbook (r'data.xls').sheet_by_name('Sheet2')
# for multiple files instead of sheets remove .sheet_by_name() and change the path

for rownum in range(max(df1.nrows, df2.nrows)):
    if rownum < df1.nrows:
        row_rb1 = df1.row_values(rownum)
        row_rb2 = df2.row_values(rownum)

        for colnum, (c1, c2) in enumerate(zip_longest(row_rb1, row_rb2)):
            if c1 != c2:
                print("Row " + str(rownum+1) + " Col " + str(colnum+1) + " - " + str(c1) +" != " + str(c2))
    else:
        print("Row " + str(rownum+1) + " missing")