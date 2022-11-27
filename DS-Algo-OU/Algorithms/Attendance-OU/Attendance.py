
from flask import Flask, render_template, request

import mysql.connector

# Flask framework is used to create web applications using python

# creating an object ot host web app using flask api
app = Flask(__name__)

# creating an object to connect to MySQL
mysql = mysql.connector.connect(host = 'Vedhanth.mysql.pythonanywhere-services.com', user = 'Vedhanth', password = 'gurram123', database = 'Vedhanth$default')


# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()
def CreateTable():
    try:
        mycursor.execute("CREATE TABLE Attendance_December (RollNo VARCHAR(255))")

        roll_no = 1
        while(roll_no <= 87):

            if(roll_no <= 65 or roll_no >= 81):
                mycursor.execute('INSERT INTO Attendance_December (RollNo) VALUES ({})'.format(roll_no))

            roll_no += 1

        mysql.commit()

        return ("Table Created")
    except Exception as e:
        return (e.msg)


# Function to display home page
@app.route('/', methods=['GET', 'POST'])
def HomePage():
    return render_template('HomePage.html')

# Function to display the data
@app.route('/View_Attendance', methods=['GET', 'POST'])
def View_Attendance():

    mycursor.execute('select * from Attendance_December')
    myresult = mycursor.fetchall()
    length = len(myresult[0])

    return render_template('ViewAttendance.html', Data=myresult, len=length)

# Function to take data from user
@app.route('/InputData', methods=["POST", "GET"])
def Input_Data():

    if request.method == 'POST':
        date = request.form['date']
        absenties = request.form['Absenties']
        absenties = list(map(lambda x: int(x), absenties))

        mycursor.execute("alter table Attendance_December add column Date_{} varchar(255)".format(date))

        for x in range(1,88):
            if(x in absenties):
                mycursor.execute("insert into Attendance_December (Date_{0}) values ({1}) where RollNo = {2}".format(date, 0, x))
            else:
                mycursor.execute("insert into Attendance_December (Date_{0}) values ({1}) where RollNo = {2}".format(date, 1, x))

        mysql.commit()
        return "Added data successfully check in 'View Attendance' Page. Thank You!"

    return render_template('InputForm.html')

# Function to create table for new month
@app.route('/Initialize', methods=['GET','POST'])
def Initialize():
    return CreateTable()
