# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:54:19 2022

@author: sshri
"""

import mysql.connector
import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="*******"
)
print(mydb)
mycursor = mydb.cursor()

# ___________________Query_________________________
mycursor.execute("CREATE DATABASE db1")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#________________________Connecting to the created db and creating tables__________________
mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="*********",
  database="db1"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Registrations (email VARCHAR(255), \
                 enabled BOOLEAN, registrationtype VARCHAR(255), \
                 usertype VARCHAR(100), PRIMARY KEY (email))")
mycursor.execute("CREATE TABLE Client (email VARCHAR(255),\
                 clientcode VARCHAR(100), userType VARCHAR(100), \
                 accepted BOOLEAN, role VARCHAR(255), inviter VARCHAR(100),\
                 CONSTRAINT c_pk PRIMARY KEY (email,accepted))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#___________________Altering tables____________________________
mycursor.execute("ALTER TABLE Registrations MODIFY COLUMN enabled VARCHAR(50)")
mycursor.execute("ALTER TABLE Client MODIFY COLUMN accepted VARCHAR(50)")

#__________________Inserting values from csv to Reg table_______________

csv_data = csv.reader(open("Desktop/registrations.csv"))
header = next(csv_data)

for row in csv_data:
    print(row)
    mycursor.execute(
        "INSERT INTO Registrations (email,enabled,registrationtype,usertype) \
        VALUES (%s, %s, %s, %s)", row)
    
mydb.commit()
mycursor.execute("SELECT * FROM Registrations")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#_____________________Inserting values into Client table from csv______________

csv_data2 = csv.reader(open("Desktop/clientuserinvites.csv"))
header = next(csv_data2)

for row in csv_data2:
    print(row)
    mycursor.execute(
        "INSERT INTO Client (email,clientcode,userType,accepted,role,inviter) \
         VALUES (%s, %s, %s, %s, %s, %s)", row)
    
mydb.commit()
mycursor.execute("SELECT * FROM Client")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()