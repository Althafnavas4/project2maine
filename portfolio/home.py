from flask import Flask, render_template, request, redirect, url_for  # Flask (classname)
from flask_mail import Mail, Message
import sqlite3

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'abhishekbinish86@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'xewq osgl gtnw sinz'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'nalthaf13@gmail.com'

mail = Mail(app)

# Database setup
con = sqlite3.connect('database.db')
try:
    con.execute('CREATE TABLE contact (name TEXT, email TEXT, phone TEXT, message TEXT)')
except:
    pass

@app.route('/')
def fun1():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def fun2():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['number']
        message = request.form['message']
        
        # Save to database
        con = sqlite3.connect('database.db')
        con.execute("INSERT INTO contact(name, email, phone, message) VALUES (?, ?, ?, ?)", 
                    (name, email, phone, message))
        con.commit()
        
        # Send email
        msg = Message(
            subject='Connect through Portfolio',
            recipients=['abhishekbinish86@gmail.com'],  # Change to your recipient email
            body=f"""
            Connect through Portfolio:
            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
        )
        mail.send(msg)
        
        print(name, email, phone, message)
        return redirect(url_for('fun1'))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
