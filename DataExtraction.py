from itertools import product
import xlrd
import os
import json

info_list = []
#gia kathe etos vriskoume to sunoliko plithismo touristwn apo oles tis xwres
for year in range(2011,2014):
    #anoigma tou arxeiou tou etous year
    file_path = ('excelFiles/'+str(year)+'/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης '+str(year)+'.xls')
    #anoigma sheet me ta telika apotelesmata tis xronias (dekemvriou)
    exfile = xlrd.open_workbook(file_path)
    sheet = exfile.sheet_by_name("ΔΕΚ")
    #anazhthsh tou genikou synolou tis telikhs statistikhs gia thn periodo ianouariou - dekemvriou kathe etous
    flag = 0
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            #anagnwrisi pinaka statistikhs gia thn periodo ianouarios - dekemvrios
            if('Ιανουάριος-Δεκέμβριος' in str(sheet.cell_value(row,col))):
                flag = 1
            if(sheet.cell_value(row,col) == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and flag):
                #print(year)
                tourists = round(sheet.cell_value(row,col+2))
                info_list.append({'year':year,'total_tourists':tourists})

for x in info_list:
    print(x.get('year'),x.get('total_tourists'))
    

