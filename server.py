#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    client_first_name = request.form['first_name']
    client_last_name = request.form['last_name']
    strawberry_total = request.form['strawberry']
    apple_total = request.form['apple']
    raspberry_total = request.form['raspberry']
    fruit_total = int(strawberry_total) + int(apple_total) + int(raspberry_total)
    student_id = request.form['student_id']
    current_datetime =datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # session['apple'] = request.form['apple']
    # session['strawberry'] = request.form['strawberry']
    # session['rasberry'] = request.form['rasberry']
    return render_template("checkout.html", first_name=client_first_name, last_name=client_last_name,
    fruit_total=fruit_total, strawberry_total = strawberry_total, apple_total=apple_total, raspberry_total=raspberry_total,
    student_id=student_id, current_datetime=current_datetime)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    