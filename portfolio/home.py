from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import sqlite3

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'nalthaf13@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'qkxemdhpbcoszkbu'  # Your email password (Use an App Password)
app.config['MAIL_DEFAULT_SENDER'] = 'nalthaf13@gmail.com'  # Default sender

mail = Mail(app)  # Initialize Flask-Mail

# Function to get database connection
def get_db_connection():
    return sqlite3.connect('database.db')

# Create table if it doesn't exist
with get_db_connection() as con:
    con.execute('CREATE TABLE IF NOT EXISTS contact (name TEXT, email TEXT, phone TEXT, message TEXT)')

# Home route (index)
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Resume page route
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Projects page route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Capture form data
        name = request.form['name']
        email = request.form['email']
       
        message = request.form['message']

        # Create the email message
        msg = Message(
            'New Message from Contact Form',
            sender=app.config['MAIL_DEFAULT_SENDER'],  # Use the default sender
            recipients=['nalthaf13@gmail.com']
        )
        msg.body = f"Message from {name} ({email}):\n\n{message}"

        # Send the email
        try:
            mail.send(msg)
            return redirect(url_for('thank_you'))
        except Exception as e:
            print(f"Error sending email: {e}")
            return f"There was an issue sending your message: {e}"

    return render_template('contact.html')

# Thank you page
@app.route('/thank_you')
def thank_you():
    return "Thank you for your message!"

if __name__ == "__main__":
    app.run(debug=True)
