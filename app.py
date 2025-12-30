"""
Student Information Portal - Flask Web Application
Main application file that handles all routes and logic.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import sys # Added for deployment readiness check

# Initialize Flask application
app = Flask(__name__)
# IMPORTANT: In a real environment, load this from an environment variable!
app.secret_key = os.environ.get('SECRET_KEY', 'default_development_key_12345') 

# Configuration
DATA_FILE = 'students.json'


# ============================================================================
# HELPER FUNCTIONS (File Persistence - CRITICAL DEPLOYMENT ISSUE HERE)
# ============================================================================

# NOTE: For deployment, these functions MUST be refactored to use a persistent
# database (like SQLite, PostgreSQL, or a cloud service) instead of a local JSON file.

def initialize_data_file():
    """
    Initialize the JSON file if it doesn't exist.
    """
    # This entire block will fail to maintain state on Heroku/cloud host.
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump([], file, indent=4)
            print(f"Created new data file: {DATA_FILE}", file=sys.stderr)
        except Exception as e:
             # If Heroku's filesystem is read-only, this will throw an error.
             print(f"Deployment Warning: Failed to initialize data file on ephemeral filesystem: {e}", file=sys.stderr)


def read_students():
    """ Read all student records from JSON file. """
    try:
        with open(DATA_FILE, 'r') as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        initialize_data_file()
        return []
    except json.JSONDecodeError:
        print("Warning: Invalid JSON in data file", file=sys.stderr)
        return []


def write_students(students):
    """ Write student records to JSON file. """
    try:
        # **This file write operation WILL BE LOST after a dyno restart on Heroku.**
        with open(DATA_FILE, 'w') as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"Error writing to file: {str(e)}", file=sys.stderr)
        # Re-raise the exception to indicate the operation failed
        raise 


def find_student_by_roll_no(roll_no):
    """ Search for a student by roll number. """
    students = read_students()
    for student in students:
        if student['roll_no'].lower() == roll_no.lower():
            return student
    return None


# ============================================================================
# FLASK ROUTES (Unchanged)
# ============================================================================

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        roll_no = request.form.get('roll_no', '').strip()
        department = request.form.get('department', '').strip()
        email = request.form.get('email', '').strip()
        
        if not all([name, roll_no, department, email]):
            flash('All fields are required!', 'error')
            return render_template('add.html')
        
        if '@' not in email or '.' not in email:
            flash('Invalid email format!', 'error')
            return render_template('add.html')
        
        if find_student_by_roll_no(roll_no):
            flash(f'Roll number {roll_no} already exists!', 'error')
            return render_template('add.html')
        
        new_student = {
            'name': name,
            'roll_no': roll_no,
            'department': department,
            'email': email
        }
        
        try:
            students = read_students()
            students.append(new_student)
            write_students(students)
            flash(f'Student {name} added successfully!', 'success')
            return redirect(url_for('view_students'))
        except Exception as e:
            # Catch file writing error (which might happen on cloud host)
            flash(f'Error adding student (Data NOT saved persistently): {str(e)}', 'error')
            return render_template('add.html')
    
    return render_template('add.html')


@app.route('/students')
def view_students():
    try:
        students = read_students()
        return render_template('students.html', students=students)
    except Exception as e:
        flash(f'Error loading students: {str(e)}', 'error')
        return render_template('students.html', students=[])


@app.route('/search', methods=['GET', 'POST'])
def search_student():
    if request.method == 'POST':
        roll_no = request.form.get('roll_no', '').strip()
        
        if not roll_no:
            flash('Please enter a roll number!', 'error')
            return render_template('search.html', student=None)
        
        student = find_student_by_roll_no(roll_no)
        
        if student:
            flash('Student found!', 'success')
            return render_template('search.html', student=student)
        else:
            flash(f'Student with roll number {roll_no} not found!', 'error')
            return render_template('search.html', student=None)
    
    return render_template('search.html', student=None)


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.errorhandler(404)
def page_not_found(e):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 - Page Not Found</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f8fafc; }
            h1 { color: #ef4444; }
            a { color: #2563eb; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <a href="/">← Return to Home</a>
    </body>
    </html>
    """, 404


@app.errorhandler(500)
def internal_error(e):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>500 - Server Error</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f8fafc; }
            h1 { color: #ef4444; }
            a { color: #2563eb; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>500 - Internal Server Error</h1>
        <p>Something went wrong on our end.</p>
        <a href="/">← Return to Home</a>
    </body>
    </html>
    """, 500


# ============================================================================
# APPLICATION ENTRY POINT
# (Cleaned up for deployment compatibility)
# ============================================================================

if __name__ == '__main__':
    # Only run the development server when executed directly (local machine)
    initialize_data_file() # Ensure students.json exists locally for testing
    print("\n" + "="*60)
    print("STUDENT INFORMATION PORTAL - FLASK APPLICATION")
    print("="*60)
    print("Starting server...")
    print("Access the application at: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    # Gunicorn ignores this line, but it's needed for local 'python app.py'
    app.run(debug=True, host='0.0.0.0', port=5000)