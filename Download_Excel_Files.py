#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import os

def download_file(link,year):
    #eksagwgh katharou link kai katevasma arxeiou excel
    href = link.get("href")
    #apothhkeush excel me to onoma kai thn xronologia an den yparxoun hdh
    if os.path.isfile('excelFiles/' + str(year) + '/' + link.get_text()+str(year)+'.xls'):
        print('excelFiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls already exists !')
    else:
        file = requests.get(str(href))
        print('excelFiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls downloaded !')
        open('excelFiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls', 'wb').write(
            file.content)


#vasiko link tis selidas gia ta statistika tou tourismou

baseUrl = 'https://www.statistics.gr/el/statistics/-/publication/STO04/'
fileUrl = []

#dhmiourgia fakelou gia thn apothikeush ton excel files
if not os.path.exists('excelFiles'):
    os.makedirs('excelFiles')

#gemisma tou fileUrl[] me ta urls gia kathe etos --> baseUrl+year+Q4
#dhmioyrgia directory kathe etous
for year in range(2011,2016):
    fileUrl.append(baseUrl+str(year)+"-Q4")
    print(baseUrl+str(year)+'-Q4')
    if not os.path.exists('excelFiles/'+str(year)):
        os.makedirs('excelFiles/'+str(year))

print('----------------------------------------------------------------------------------------------')

#gia kathe url tou antistoixou etous katevazoume to html page gia ekswgwgi ton links me ta arxeia excel
#ta apothikeuoyme ston fakelo me thn swsti xronologia
year = 2011
for url in fileUrl:
    #apothikeysh html selidas gia kathe etos se kathe fakelo etous
    myfile = requests.get(url)
    open ('excelFiles/'+str(year)+'/statistics'+str(year)+'.html','wb').write(myfile.content)
    #eksagwgh olwn ton url pou periexei h selida tou antistoixou etous
    with open('excelFiles/'+str(year)+'/statistics'+str(year)+'.html','r',encoding='utf-8') as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents,'lxml')
        all_links = (soup.find_all('a'))
        print('Try to Download next files from: '+url)
        #anazitisi kai anagnwrisi ton links pou periexoun ta excel files me to parakatw string
        for link in all_links:
            if("Αφίξεις μη κατοίκων από το εξωτερικό ανά"in str(link)):
                download_file(link,year)

    year += 1
    print('----------------------------------------------------------------------------------------------')
