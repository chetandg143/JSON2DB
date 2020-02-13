import json

import mysql.connector
mydb = mysql.connector.connect( host ="localhost" , user = 'root' , password = 'MYSQL123' , database ='jsproj')

f=open("phone.json","r")
phone=json.load(f)
print(phone)

mycur = mydb.cursor()
#1
"""mycur.execute("CREATE TABLE if not exists Pdetails (c_code varchar(20) PRIMARY KEY , mobileno varchar(250)) ")
item=phone.items()


for a,b in phone.items():
    sql="INSERT INTO Pdetails VALUES(%s,%s)"
    val =(a,b)
    mycur.execute(sql,val)
    mydb.commit()
   # print(mycur.rowcount ,"row inserted!")"""


"""f=open("names.json","r")
names=json.load(f)
print(names)

#2
mycur.execute("CREATE TABLE if not exists Namelist (c_code varchar(20) PRIMARY KEY , c_name varchar(250)) ")
item=names.items()


for a,b in names.items():
    sql="INSERT INTO Namelist VALUES(%s,%s)"
    val =(a,b)
    mycur.execute(sql,val)
    mydb.commit()
"""
"""f=open("currency.json","r")
currency=json.load(f)
print(currency)

#3
mycur.execute("CREATE TABLE if not exists Currency (c_code varchar(20) PRIMARY KEY , currency varchar(250)) ")
item=currency.items()


for a,b in currency.items():
    sql="INSERT INTO Currency VALUES(%s,%s)"
    val =(a,b)
    mycur.execute(sql,val)
    mydb.commit()
"""

"""f=open("iso3.json","r")
iso=json.load(f)
print(iso)

#4
mycur.execute("CREATE TABLE if not exists Iso (c_code varchar(20) PRIMARY KEY , iso_name varchar(250)) ")
item=iso.items()


for a,b in iso.items():
    sql="INSERT INTO Iso VALUES(%s,%s)"
    val =(a,b)
    mycur.execute(sql,val)
    mydb.commit()
"""
"""f=open("continent.json","r")
conti=json.load(f)
print(conti)

#5
mycur.execute("CREATE TABLE if not exists Continent (c_code varchar(20) PRIMARY KEY , conti_name varchar(250)) ")
item=conti.items()


for a,b in conti.items():
    sql="INSERT INTO Continent VALUES(%s,%s)"
    val =(a,b)
    mycur.execute(sql,val)
  """
#mycur.execute("create view data1 as select c_name , conti_name ,iso_name from Continent , Iso ,Namelist where Continent.c_code = Iso.c_code = Namelist.c_code ")
mycur.execute("select * from data1 ")
res = mycur.fetchone()
print(res)
mydb.commit()