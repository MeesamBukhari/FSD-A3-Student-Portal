"""
Exception Handling Demonstration
This script demonstrates proper error handling for:
1. Missing files (FileNotFoundError)
2. Incorrect data format (JSONDecodeError)
3. Invalid input (ValueError)
4. General exceptions

Author: Student Information Portal
Date: November 2025
"""

import json
import os


def read_student_file(filename):
    """
    Safely read student data from JSON file with comprehensive error handling.
    
    Parameters:
        filename (str): Path to the JSON file
        
    Returns:
        list: List of student dictionaries, or empty list if error occurs
    """
    print(f"\nAttempting to read file: '{filename}'")
    print("-" * 60)
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            data = json.load(file)
        
        # Validate that data is a list
        if not isinstance(data, list):
            raise ValueError("Data must be a list of student records")
        
        # Validate each record has required fields
        required_fields = ['name', 'roll_no', 'department', 'email']
        for index, record in enumerate(data):
            for field in required_fields:
                if field not in record:
                    raise ValueError(f"Record {index} is missing required field: '{field}'")
        
        print(f"✓ SUCCESS: File read successfully")
        print(f"✓ Total records loaded: {len(data)}")
        return data
        
    except FileNotFoundError:
        # Handle missing file
        print(f"✗ ERROR: File '{filename}' not found!")
        print(f"  Creating a new empty file...")
        
        # Create new file with empty list
        try:
            with open(filename, 'w') as file:
                json.dump([], file, indent=4)
            print(f"✓ New file created successfully")
        except Exception as e:
            print(f"✗ Failed to create file: {str(e)}")
        
        return []
    
    except json.JSONDecodeError as e:
        # Handle invalid JSON format
        print(f"✗ ERROR: Invalid JSON format in file!")
        print(f"  Details: {str(e)}")
        print(f"  Line: {e.lineno}, Column: {e.colno}")
        
        # Backup corrupted file
        backup_name = f"{filename}.backup"
        try:
            os.rename(filename, backup_name)
            print(f"✓ Corrupted file backed up as '{backup_name}'")
            
            # Create new empty file
            with open(filename, 'w') as file:
                json.dump([], file, indent=4)
            print(f"✓ New empty file created")
        except Exception as backup_error:
            print(f"✗ Backup failed: {str(backup_error)}")
        
        return []
    
    except ValueError as e:
        # Handle data validation errors
        print(f"✗ ERROR: Data validation failed!")
        print(f"  Details: {str(e)}")
        return []
    
    except PermissionError:
        # Handle permission issues
        print(f"✗ ERROR: Permission denied!")
        print(f"  You don't have permission to read '{filename}'")
        return []
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"✗ UNEXPECTED ERROR: {type(e).__name__}")
        print(f"  Details: {str(e)}")
        return []
    
    finally:
        # This block always executes
        print("-" * 60)
        print("File operation completed.\n")


def safe_add_student(filename, name, roll_no, department, email):
    """
    Safely add a student record with comprehensive error handling.
    
    Parameters:
        filename (str): Path to JSON file
        name (str): Student name
        roll_no (str): Roll number
        department (str): Department name
        email (str): Email address
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"\nAttempting to add student: {name}")
    print("-" * 60)
    
    try:
        # Validate inputs
        if not all([name, roll_no, department, email]):
            raise ValueError("All fields are required and cannot be empty")
        
        if '@' not in email:
            raise ValueError(f"Invalid email format: '{email}'")
        
        # Read existing data
        students = read_student_file(filename)
        
        # Check for duplicate roll number
        for student in students:
            if student['roll_no'] == roll_no:
                raise ValueError(f"Roll number '{roll_no}' already exists")
        
        # Create new student record
        new_student = {
            'name': name,
            'roll_no': roll_no,
            'department': department,
            'email': email
        }
        
        # Add to list
        students.append(new_student)
        
        # Save to file
        with open(filename, 'w') as file:
            json.dump(students, file, indent=4)
        
        print(f"✓ SUCCESS: Student '{name}' added successfully!")
        return True
        
    except ValueError as e:
        print(f"✗ VALIDATION ERROR: {str(e)}")
        return False
    
    except json.JSONDecodeError:
        print(f"✗ ERROR: Failed to write JSON data")
        return False
    
    except Exception as e:
        print(f"✗ UNEXPECTED ERROR: {type(e).__name__} - {str(e)}")
        return False
    
    finally:
        print("-" * 60)


def demonstrate_exception_handling():
    """
    Main demonstration function showing various error scenarios.
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: EXCEPTION HANDLING")
    print("="*70)
    
    # Test 1: Reading non-existent file
    print("\nTest 1: Reading Non-Existent File")
    print("="*70)
    data = read_student_file("nonexistent_file.json")
    
    # Test 2: Reading valid file (students.json)
    print("\nTest 2: Reading Valid File")
    print("="*70)
    data = read_student_file("students.json")
    
    # Test 3: Creating corrupted JSON file and reading it
    print("\nTest 3: Reading Corrupted JSON File")
    print("="*70)
    try:
        # Create a corrupted JSON file
        with open("corrupted.json", 'w') as f:
            f.write("{ this is not valid JSON }")
        print("Created corrupted.json for testing...")
    except Exception as e:
        print(f"Failed to create test file: {e}")
    
    data = read_student_file("corrupted.json")
    
    # Test 4: Adding student with valid data
    print("\nTest 4: Adding Student with Valid Data")
    print("="*70)
    success = safe_add_student(
        "students.json",
        "Test Student",
        "CS999",
        "Computer Science",
        "test.student@paf-iast.edu.pk"
    )
    
    # Test 5: Adding student with invalid email
    print("\nTest 5: Adding Student with Invalid Email")
    print("="*70)
    success = safe_add_student(
        "students.json",
        "Invalid Student",
        "CS998",
        "Computer Science",
        "invalidemail"  # Missing @ symbol
    )
    
    # Test 6: Adding student with empty fields
    print("\nTest 6: Adding Student with Empty Fields")
    print("="*70)
    success = safe_add_student(
        "students.json",
        "",  # Empty name
        "CS997",
        "Computer Science",
        "test@email.com"
    )
    
    # Test 7: Adding duplicate roll number
    print("\nTest 7: Adding Student with Duplicate Roll Number")
    print("="*70)
    success = safe_add_student(
        "students.json",
        "Duplicate Student",
        "CS999",  # Already exists from Test 4
        "Computer Science",
        "duplicate@paf-iast.edu.pk"
    )
    
    print("\n" + "="*70)
    print("EXCEPTION HANDLING DEMONSTRATION COMPLETED")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Always use try-except blocks for file operations")
    print("2. Handle specific exceptions before general ones")
    print("3. Use finally block for cleanup operations")
    print("4. Provide meaningful error messages to users")
    print("5. Implement data validation before processing")
    print("="*70 + "\n")


# Run demonstration
if __name__ == "__main__":
    demonstrate_exception_handling()