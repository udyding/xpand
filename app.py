from flask import Flask, redirect, url_for, render_template, request, json
import sqlite3

app = Flask(__name__, template_folder='templates')

conn = sqlite3.connect('./registrants.db', check_same_thread=False)
db = conn.cursor()

@app.route("/")
def home():
    return "Hello! this is the main page"

@app.route("/showRegistration")
def showRegistration():
    return render_template('form.html')

@app.route("/registration", methods=['POST'])
def registration():
    #read posted values
    if request.method == 'POST':
        db.execute(
            'INSERT into registrants (city, name, phone, email, website, description) VALUES (?, ?, ?, ?, ?, ?)', (
                request.form.get('city'),
                request.form.get('name'),
                request.form.get('phone'),
                request.form.get('email'),
                request.form.get('website'),
                request.form.get('description'))
            )
        conn.commit()
    return render_template('redirect.html')
            
if __name__ == "__main__":
    app.debug = True
    app.run()

