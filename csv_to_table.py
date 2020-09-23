import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="guardian",
  database="test"
)

mycursor = mydb.cursor()

arr=[]
with open('student.csv','r') as data: 
	for line in csv.reader(data):
   		t=tuple(line)
   		print(t)
   		arr.append(t)
        
# print(arr)
sql = "INSERT INTO students(Name, Roll_no) VALUES (%s, %s)"
val = arr

mycursor.executemany(sql, val) 
mydb.commit() 

print(mycursor.rowcount, "details inserted") 
mydb.close() 
