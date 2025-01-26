from flask import Flask, render_template

app = Flask(__name__)

# Home route to display your portfolio
@app.route('/')
def home():
    # Add your projects here
    projects = [
        {'title': 'Project 1', 'description': 'Brief description of Project 1', 'image': 'project1.jpg'},
        {'title': 'Project 2', 'description': 'Brief description of Project 2', 'image': 'project2.jpg'}
    ]
    
    # Add your skills here
    skills = ['Python', 'Flask', 'HTML/CSS', 'JavaScript', 'React']

    # Contact information (Add your contact details here)
    contact = {
        'email': 'your.email@example.com',
        'linkedin': 'https://linkedin.com/in/yourprofile',
        'github': 'https://github.com/yourprofile'
    }

    # Render the index.html template with the projects, skills, and contact information
    return render_template('index.html', projects=projects, skills=skills, contact=contact)

# About route (Optional: You can add an About page to describe yourself)
@app.route('/about')
def about():
    about_info = "Write a brief introduction about yourself, your background, experience, etc."
    return render_template('about.html', about_info=about_info)

if __name__ == '__main__':
    app.run(debug=True)
