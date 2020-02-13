import json

import  mysql.connector

mydb = mysql.connector.connect( host ="localhost" , user ='root' ,password ='MYSQL123' ,database ='de')
mycur = mydb.cursor()

#1
"""fi = open("phone.json" , "r")
phone =json.load(fi)
print(phone)

#mycur.execute("create table  P (code varchar(50) , nor varchar(50) , PRIMARY KEY (code))")
item =phone.items()
for a , b in phone.items():
    query = "INSERT INTO P VALUES(%s, %s)"
    val =(a,b)
    mycur.execute(query , val)
    mydb.commit()"""

#2
"""fi = open("names.json" , "r")
names =json.load(fi)
print(names)

mycur.execute("create table  N (code varchar(50) , cnames varchar(50) , FOREIGN KEY (code) REFERENCES P (code))")
item =names.items()
for a , b in names.items():
    query = "INSERT INTO N VALUES(%s, %s)"
    val =(a,b)
    mycur.execute(query , val)
    mydb.commit()

"""
#3
"""fi = open("iso3.json" , "r")
iso =json.load(fi)
print(iso)

mycur.execute("create table  I (code varchar(50) , isonames varchar(50) , FOREIGN KEY (code) REFERENCES P (code))")
item =iso.items()
for a , b in iso.items():
    query = "INSERT INTO I VALUES(%s, %s)"
    val =(a,b)
    mycur.execute(query , val)
    mydb.commit()
"""

#4
"""fi = open("currency.json" , "r")
cur =json.load(fi)
print(cur)

mycur.execute("create table  C (code varchar(50) , currency varchar(50) , FOREIGN KEY (code) REFERENCES P (code))")
item =cur.items()
for a , b in cur.items():
    query = "INSERT INTO C VALUES(%s, %s)"
    val =(a,b)
    mycur.execute(query , val)
    mydb.commit()"""

#5
"""fi = open("continent.json" , "r")
conti =json.load(fi)
print(conti)

mycur.execute("create table  Conti (code varchar(50) , conti varchar(50) , FOREIGN KEY (code) REFERENCES P (code))")
item =conti.items()
for a , b in conti.items():
    query = "INSERT INTO Conti VALUES(%s, %s)"
    val =(a,b)
    mycur.execute(query , val)
    mydb.commit()
"""

mycur.execute("create view p as select P.code , nor , cnames , currency ,isonames ,conti from P , N, C, I ,Conti where P.code = N.code = C.code = I.code =Conti.code  limit 300 ")
mycur.execute("select * from p ")
res = mycur.fetchall()
print(res)
