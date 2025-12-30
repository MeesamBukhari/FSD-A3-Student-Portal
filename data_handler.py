"""
Data Handling and File Management Script
This script provides functionality to:
1. Add new student records
2. Display all records
3. Search for a record by roll number

Author: Student Information Portal
Date: November 2025
"""

import json
import os

# Constants
DATA_FILE = 'students.json'


def initialize_file():
    """
    Initialize the JSON file if it doesn't exist.
    Creates an empty list to store student records.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump([], file, indent=4)
        print(f"✓ Created new data file: {DATA_FILE}")


def add_record():
    """
    Add a new student record to the JSON file.
    Prompts user for input and validates data before storing.
    """
    try:
        print("\n" + "="*50)
        print("ADD NEW STUDENT RECORD")
        print("="*50)
        
        # Get input from user
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number (e.g., CS101): ").strip()
        department = input("Enter department: ").strip()
        email = input("Enter email address: ").strip()
        
        # Validate input
        if not all([name, roll_no, department, email]):
            print("✗ Error: All fields are required!")
            return
        
        if '@' not in email:
            print("✗ Error: Invalid email format!")
            return
        
        # Read existing records
        with open(DATA_FILE, 'r') as file:
            students = json.load(file)
        
        # Check for duplicate roll number
        for student in students:
            if student['roll_no'] == roll_no:
                print(f"✗ Error: Roll number {roll_no} already exists!")
                return
        
        # Create new student record
        new_student = {
            'name': name,
            'roll_no': roll_no,
            'department': department,
            'email': email
        }
        
        # Add to list
        students.append(new_student)
        
        # Write back to file
        with open(DATA_FILE, 'w') as file:
            json.dump(students, file, indent=4)
        
        print(f"\n✓ Student {name} added successfully!")
        print("="*50)
        
    except FileNotFoundError:
        print("✗ Error: Data file not found. Initializing new file...")
        initialize_file()
        add_record()
    except json.JSONDecodeError:
        print("✗ Error: Invalid JSON format in file!")
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")


def display_all_records():
    """
    Display all student records from the JSON file.
    Shows data in a formatted table.
    """
    try:
        with open(DATA_FILE, 'r') as file:
            students = json.load(file)
        
        if not students:
            print("\n" + "="*80)
            print("No student records found!")
            print("="*80)
            return
        
        # Display header
        print("\n" + "="*80)
        print("ALL STUDENT RECORDS")
        print("="*80)
        print(f"{'#':<5} {'Name':<25} {'Roll No':<15} {'Department':<20} {'Email':<25}")
        print("-"*80)
        
        # Display each record
        for index, student in enumerate(students, 1):
            print(f"{index:<5} {student['name']:<25} {student['roll_no']:<15} "
                  f"{student['department']:<20} {student['email']:<25}")
        
        print("="*80)
        print(f"Total Students: {len(students)}")
        print("="*80 + "\n")
        
    except FileNotFoundError:
        print("✗ Error: Data file not found!")
        initialize_file()
    except json.JSONDecodeError:
        print("✗ Error: Invalid JSON format in file!")
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")


def search_by_roll_number():
    """
    Search for a student by roll number.
    Displays the student information if found.
    """
    try:
        roll_no = input("\nEnter roll number to search: ").strip()
        
        if not roll_no:
            print("✗ Error: Roll number cannot be empty!")
            return
        
        with open(DATA_FILE, 'r') as file:
            students = json.load(file)
        
        # Search for student
        found = False
        for student in students:
            if student['roll_no'].lower() == roll_no.lower():
                print("\n" + "="*60)
                print("STUDENT FOUND")
                print("="*60)
                print(f"Name:        {student['name']}")
                print(f"Roll Number: {student['roll_no']}")
                print(f"Department:  {student['department']}")
                print(f"Email:       {student['email']}")
                print("="*60 + "\n")
                found = True
                break
        
        if not found:
            print(f"\n✗ Student with roll number '{roll_no}' not found!")
        
    except FileNotFoundError:
        print("✗ Error: Data file not found!")
        initialize_file()
    except json.JSONDecodeError:
        print("✗ Error: Invalid JSON format in file!")
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")


def main_menu():
    """
    Display main menu and handle user choices.
    """
    # Initialize file on startup
    initialize_file()
    
    while True:
        print("\n" + "="*50)
        print("STUDENT INFORMATION MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add a new record")
        print("2. Display all records")
        print("3. Search for a record by roll number")
        print("4. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_record()
        elif choice == '2':
            display_all_records()
        elif choice == '3':
            search_by_roll_number()
        elif choice == '4':
            print("\n✓ Thank you for using the system. Goodbye!")
            break
        else:
            print("\n✗ Invalid choice! Please enter 1-4.")


# Run the program
if __name__ == "__main__":
    main_menu()