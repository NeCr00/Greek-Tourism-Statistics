from itertools import product
import xlrd
<<<<<<< HEAD
import SqlConnector as db
import DBManager
import csv
import pandas as pd

def csv_output_file(fieldnames,filename,table_name):
    mycursor = db.mycursor
    mycursor.execute("SELECT * FROM "+table_name)
    myresult = mycursor.fetchall()
    df =pd.DataFrame(myresult,columns=fieldnames)
    df.to_csv(filename, encoding='utf-8-sig')
    print(df)

def synolikes_afikseis_touristwn (year,row,col,total_arrivals,sheet):
    #h sthlh me tis synolikes afikseis ths swsths xronias einai 2 sthles dipla apo thn sthlh pou periexei to geniko synolo
    tourists = round(sheet.cell_value(row, col + 2))
    sql = "INSERT IGNORE INTO tourism_per_year (year,total_tourists) VALUES(%s,%s)"
    val = (year,tourists)
    db.mycursor.execute(sql,val)
    db.mydb.commit()
    #print("Sucessful Parse of Data in table tourism_per_year")
    csv_output_file(['ΕΤΟΣ','ΣΥΝΟΛΙΚΟΙ ΤΟΥΡΙΣΤΕΣ'],"ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΓΙΑ ΤΟ 2011-2013.csv","tourism_per_year")

def xwra_touristwn_me_megalyterh_afiksh(percentage,typeofcell,country,year,max_country_per_year):

    count = 1 #voithitikos metrhths gia thn anagnwrish xwras
    max_percentage = 0 #megisto pososto
    max_country = 'None' #onoma xwras me to megalutero pososto
    for i in range(len(typeofcell)):
        #an to cell exei timh arithmo tote h seira antistoixei se xwra
        if(str(count) in typeofcell[i].value):
            if(percentage[i].value > max_percentage):
                max_percentage = percentage[i].value
                max_country = country[i].value
            count +=1


    #max_country_per_year.append({'year':year,'max_country':str(max_country),'percentage':max_percentage})
    sql = "INSERT IGNORE INTO country_most_tourists (year,country,percentage) VALUES(%s,%s,%s)"
    val = (year, max_country,max_percentage)
    db.mycursor.execute(sql, val)
    db.mydb.commit()
    csv_output_file(['ΕΤΟΣ', 'ΧΩΡΑ','ΠΟΣΟΣΤΟ'], "ΧΩΡΕΣ ΤΟΥΡΙΣΤΩΝ ΜΕ ΤΗΝ ΜΕΓΑΛΥΤΕΡΗ ΑΠΗΧΗΣΗ ΓΙΑ ΤΟ 2011-2013.csv", "country_most_tourists")

def synolikes_afikseis_ana_meso(year,row,col,total_arrivals_by_means,sheet):
    by_air = round(sheet.cell_value(row,col+1))
    by_train = round(sheet.cell_value(row,col+2))
    by_sea = round(sheet.cell_value(row,col+3))
    by_road = round(sheet.cell_value(row,col+4))
    #total_arrivals_by_means.append({'year':year,'by-air':by_air,'by_train':by_train,'by_sea':by_sea,'by_road':by_road})
    sql = "INSERT IGNORE INTO tourists_by_means (year,by_air,by_train,by_sea,by_road) VALUES(%s,%s,%s,%s,%s)"
    val = (year,by_air,by_train,by_sea,by_road)
    db.mycursor.execute(sql, val)
    db.mydb.commit()
    #print("Sucessful Parse of Data in table country_most_tourists")
    csv_output_file(['ΧΡΟΝΙΑ','ΑΕΡΙΠΟΡΙΚΟΣ','ΣΙΔ/ΚΩΣ','ΘΑΛΑΣΣΙΩΣ','ΟΔΙΚΟΣ'], "ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΑΝΑ ΜΕΣΟ ΓΙΑ ΤΟ 2011-2013.csv","tourists_by_means")

def synolikes_afikseis_ana_trimhno(year, row, col, total_arrivals_by_semester, sheet, i):
        prev_total = 0;
        if (i == 2):
            total_tourists = round(sheet.cell_value(row, col + 2))
            semester = 1
        else:
            for info in total_arrivals_by_semester:
                prev_total = prev_total + info.get('total_tourists')

            total_tourists = round(sheet.cell_value(row, col + 2) - prev_total)
            semester = total_arrivals_by_semester[len(total_arrivals_by_semester) - 1].get('semester') + 1

        total_arrivals_by_semester.append({'year': year, 'semester': semester, 'total_tourists': total_tourists})
        sql = "INSERT IGNORE INTO tourism_per_semester (year,semester,total_tourists) VALUES(%s,%s,%s)"
        val = (year,semester,total_tourists)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        csv_output_file(['ΧΡΟΝΙΑ','ΤΡΙΜΗΝΟ','ΣΥΝΟΛΙΚΟΙ ΤΟΥΡΙΣΤΕΣ'],"ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΑΝΑ ΤΡΙΜΗΝΟ ΓΙΑ ΤΟ 2011-2013.csv", "tourism_per_semester")


#apothikeuei gia kathe xronia synoliko tourismo
total_arrivals = []
#apothikeyei ta stoixeia ana etos gia thn xwra me to megalutero pososto
max_country_per_year = []
#gia kathe etos vriskoume to sunoliko plithismo touristwn apo oles tis xwres kai thn xwra me to megalutero pososto summetoxhs
=======
import os
import json

info_list = []
#gia kathe etos vriskoume to sunoliko plithismo touristwn apo oles tis xwres
>>>>>>> 49d6e73683c248439fb0d27ba8fecd7d88ee906b
for year in range(2011,2014):
    #anoigma tou arxeiou tou etous year
    file_path = ('excelFiles/'+str(year)+'/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης '+str(year)+'.xls')
    #anoigma sheet me ta telika apotelesmata tis xronias (dekemvriou)
    exfile = xlrd.open_workbook(file_path)
    sheet = exfile.sheet_by_name("ΔΕΚ")
    #anazhthsh tou genikou synolou tis telikhs statistikhs gia thn periodo ianouariou - dekemvriou
    flag = 0
    #anazhthsh me for loop se ola ta cell tou sheet
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            #anagnwrisi pinaka statistikhs gia thn periodo ianouarios - dekemvrios kai energopoihsh flag
            if('Ιανουάριος-Δεκέμβριος' in str(sheet.cell_value(row,col))):
                flag = 1
            # anagnwrish tou pinaka twn pososton
            if('Aναλογία επί του συνόλου' in str(sheet.cell_value(row,col)) and flag):

                #antigrafh ths sthlhs me ta pososta afikshs touristwn ana xwra
                percentage= sheet.col_slice(col+1,row)
                #antigrafh prwths sthlhs,xrhsimopoeitai gia na anagnwrisei an prokeitai gia xwra
                typeofcell=sheet.col_slice(0,row)
                #antigrafh deuterhs sthlhs gia thn euresh tou onomatos ths xwras
                country= (sheet.col_slice(1,row))
                #euresh xwras me to megalytero pososto afiksewn
                xwra_touristwn_me_megalyterh_afiksh(percentage,typeofcell,country,year,max_country_per_year)

            if(sheet.cell_value(row,col) == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and flag):
<<<<<<< HEAD
                synolikes_afikseis_touristwn(year,row,col,total_arrivals,sheet)



print(max_country_per_year)
print(total_arrivals)

total_arrivals_by_means = []
#-=============================================================================================================================================================



for year in range(2011,2014):
    #anoigma tou arxeiou tou etous year
    file_path = ('excelFiles/'+str(year)+'/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης και μέσο μεταφοράς '+str(year)+'.xls')
    #anoigma sheet me ta telika apotelesmata tis xronias (dekemvriou)
    exfile = xlrd.open_workbook(file_path)
    sheet = exfile.sheet_by_name("ΔΕΚ")
    #anazhthsh tou genikou synolou tis telikhs statistikhs gia thn periodo ianouariou - dekemvriou
    flag = 0
    #anazhthsh me for loop se ola ta cell tou sheet
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            #anagnwrisi pinaka statistikhs gia thn periodo ianouarios - dekemvrios kai energopoihsh flag
            if('ΠΕΡΙΟΔΟΣ:Ιανουάριος' in str(sheet.cell_value(row,col))):
                flag = 1
            if(sheet.cell_value(row,col) == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and flag):
                synolikes_afikseis_ana_meso(year,row,col,total_arrivals_by_means,sheet)

print(total_arrivals_by_means)


total_arrivals_by_semester = []

for year in range(2011,2014):
        #anoigma tou arxeiou tou etous year
        file_path = ('excelFiles/'+str(year)+'/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης '+str(year)+'.xls')
        #anoigma sheet me ta telika apotelesmata tis xronias (dekemvriou)
        exfile = xlrd.open_workbook(file_path)
        for i in range(2,12,3):
            sheet = exfile.sheet_by_index(i)
            #anazhthsh tou genikou synolou tis telikhs statistikhs gia thn periodo ianouariou - dekemvriou
            flag = 0
            #anazhthsh me for loop se ola ta cell tou sheet
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    #anagnwrisi pinaka statistikhs gia thn periodo ianouarios - dekemvrios kai energopoihsh flag
                    if('ΠΕΡΙΟΔΟΣ: Ιανουάριος' in str(sheet.cell_value(row,col))):
                        flag = 1


                    if(sheet.cell_value(row,col) == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and flag):

                        synolikes_afikseis_ana_trimhno(year,row,col,total_arrivals_by_semester,sheet,i)
        total_arrivals_by_semester = []
print(total_arrivals_by_semester)



=======
                #print(year)
                tourists = round(sheet.cell_value(row,col+2))
                info_list.append({'year':year,'total_tourists':tourists})

for x in info_list:
    print(x.get('year'),x.get('total_tourists'))
    
>>>>>>> 49d6e73683c248439fb0d27ba8fecd7d88ee906b

