from calendar import calendar
from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.now()
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    global name
    name = request.form['name']
    return render_template('form.html', name=name)


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    display = ""
    # Write your to code here to check whether number is even or odd and render result.html page
    if number % 2 == 1:
        return render_template('result.html', display="Number {Number} is even")
    elif number % 2 == 0:
        return render_template('result.html', display="Number {Number} is odd")
    elif number == None:
        return render_template('result.html', display="No number provided")
    else: 
        return render_template('result.html', display="Provided input is not an integer!")

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentDetails.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    organizationName = request.form['orgName']
    # Append this value to studentOrganisationDetails
    combined = studentName + organizationName
    # Display studentDetails.html with all students and organisations
    return render_template('studentDetails.html', combined = combined)