import mysql.connector

mydb = mysql.connector.connect(user='root', password='giannis007',
                              port ='3306',
                              host='127.0.0.1',
                              auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Tourism_Statistics CHARACTER SET utf8 COLLATE utf8_general_ci;")
mycursor.execute("USE Tourism_Statistics")
#mycursor.execute("ALTER DATABASE tourism_statistics CHARACTER SET utf8 COLLATE utf8_general_ci;")
mycursor.execute("CREATE TABLE  IF NOT EXISTS tourism_per_year(year INT NOT NULL PRIMARY KEY,total_tourists INT)")
mycursor.execute("CREATE TABLE  IF NOT EXISTS country_most_tourists(year INT NOT NULL PRIMARY KEY,country VARCHAR(50),percentage FLOAT)")
mycursor.execute("CREATE TABLE  IF NOT EXISTS tourists_by_means(year INT NOT NULL PRIMARY KEY,by_air INT,by_train INT,by_sea INT,by_road INT)")
mycursor.execute("CREATE TABLE  IF NOT EXISTS tourism_per_semester(year INT NOT NULL,semester INT NOT NULL ,total_tourists INT, CONSTRAINT TOUR_SEM PRIMARY KEY (year,semester))")


print(mydb)