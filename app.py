import sys
import csv
from flask import Flask, redirect, request, render_template

## To install run: pip install Flask-MySQL --user
from flaskext.mysql import MySQL

# =================== database setup ===================

global MYSQL_DATABASE_USER
global MYSQL_DATABASE_PASSWORD
global MYSQL_DATABASE_DB
global MYSQL_DATABASE_HOST

# reads in data from csv
def getDatabaseInfo():
    with open('./resources/database.csv', 'rb') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',' , quotechar= '|')
        # Reads in the rows of csv and creates a new duck object for each row
        for row in readcsv:
            global MYSQL_DATABASE_USER
            global MYSQL_DATABASE_PASSWORD
            global MYSQL_DATABASE_DB
            global MYSQL_DATABASE_HOST
            MYSQL_DATABASE_USER = row[0]
            MYSQL_DATABASE_PASSWORD = row[1]
            MYSQL_DATABASE_DB = row[2]
            MYSQL_DATABASE_HOST = row[3]

app = Flask(__name__)

getDatabaseInfo()
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
mysql.init_app(app)

# =================== data Class ===================

#Creating class of students for data to be stored in a python object
class Student:

    # Objects of this class will have a name, price , score and image

    def __init__(self, firstName, surname, mobileNumber):
        self.firstName = firstName
        self.surname = surname
        self.mobileNumber = mobileNumber


global studentList
studentList = []

# =================== Website ===================

homepage = "index.html"

@app.route("/")
def main():
    return "Welcome"

@app.route("/data")
def getHome():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    for student in  data:
        newStudent = Student(student[1], student[2], student[3])
        studentList.append(newStudent)
    return render_template(homepage, list = studentList)



# =================== Server startup ===================

if __name__ == "__main__":
    app.run()

