# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:04:45 2022

@author: sshri
"""

import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="***********",
  database="db1"
)
mycursor = mydb.cursor()

colm=[]
row=[]

sql = "SELECT \
  Client.clientcode AS 'Client Code', \
  COUNT(Registrations.email) AS 'Number of users on spottabl' \
  FROM Client INNER JOIN Registrations ON Client.email = Registrations.email \
  GROUP BY Client.clientcode "

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    row.extend(x)

for i in mycursor.description:
    colm.append(i[0])
  

sql = "SELECT \
  COUNT(Client.email) AS 'Number of users invited from spottabl' \
  FROM Client GROUP BY Client.clientcode "

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  row.extend(x)
for i in mycursor.description:
    colm.append(i[0])
    
sql = "SELECT \
  COUNT(Client.email) AS 'Number of users who have accepted invite' \
  FROM Client WHERE accepted='TRUE' GROUP BY Client.clientcode "

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  row.extend(x)
for i in mycursor.description:
    colm.append(i[0])


sql = "SELECT \
  COUNT(Client.email) AS 'Number of users invited from spottabl user' \
  FROM Client WHERE inviter LIKE '%spottabl%' GROUP BY Client.clientcode "

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  row.extend(x)
for i in mycursor.description:
    colm.append(i[0])

print(colm)
print(row)

fp= open('Result_set.csv','w')
myFile= csv.writer(fp, lineterminator='\n')
myFile.writerow(colm)
myFile.writerow(row)
fp.close()
mycursor.close()