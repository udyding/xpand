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

@app.route("/browse/<name>", methods=['GET', 'POST'])
def business(name):
    db.execute('SELECT city, name, phone, email, website, description FROM registrants WHERE name = ?', (name,))
    tempinfo = db.fetchone()
    
    business = {
        'city': tempinfo[0],
        'name': tempinfo[1],
        'phone': tempinfo[2],
        'email': tempinfo[3],
        'website': tempinfo[4],
        'description': tempinfo[5] 
    }

    return render_template('generalbusiness.html', business=business)

@app.route('/businesses', methods=['GET'])
def businesses():
    db.execute('SELECT * FROM registrants')
    tempinfo = db.fetchall()
    businesses = [{
        'city': business[0],
        'name': business[1],
        'phone': business[2],
        'email': business[3],
        'website': business[4],
        'description': business[5]
    } for business in tempinfo]
    print(businesses)
    return render_template('business.html', businesses=businesses)

if __name__ == "__main__":
    app.debug = True
    app.run()

