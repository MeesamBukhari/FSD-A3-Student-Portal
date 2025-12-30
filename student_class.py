"""
Object-Oriented Design - Student Class
This script demonstrates OOP principles including:
- Class definition with attributes
- Instance methods
- Creating multiple objects
- Method invocation

Author: Student Information Portal
Date: November 2025
"""


class Student:
    """
    Student class to represent a student with their information.
    
    Attributes:
        name (str): Student's full name
        roll_no (str): Unique roll number
        department (str): Department name
        email (str): Email address
    """
    
    # Class variable - shared across all instances
    total_students = 0
    
    def __init__(self, name, roll_no, department, email):
        """
        Constructor to initialize a Student object.
        
        Parameters:
            name (str): Student's full name
            roll_no (str): Unique roll number
            department (str): Department name
            email (str): Email address
        """
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.email = email
        
        # Increment total students count
        Student.total_students += 1
    
    def display_info(self):
        """
        Display complete student information in a formatted way.
        This is an instance method that operates on the object's data.
        """
        info = f"""
        {'='*50}
        STUDENT INFORMATION
        {'='*50}
        Name:        {self.name}
        Roll Number: {self.roll_no}
        Department:  {self.department}
        Email:       {self.email}
        {'='*50}
        """
        print(info)
    
    def update_email(self, new_email):
        """
        Update the student's email address with validation.
        
        Parameters:
            new_email (str): New email address
            
        Returns:
            bool: True if update successful, False otherwise
        """
        # Validate email format
        if '@' not in new_email or '.' not in new_email:
            print(f"✗ Error: Invalid email format '{new_email}'")
            return False
        
        old_email = self.email
        self.email = new_email
        print(f"✓ Email updated successfully!")
        print(f"  Old: {old_email}")
        print(f"  New: {new_email}")
        return True
    
    def get_details(self):
        """
        Return student details as a dictionary.
        Useful for JSON serialization.
        
        Returns:
            dict: Student information
        """
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'department': self.department,
            'email': self.email
        }
    
    @classmethod
    def get_total_students(cls):
        """
        Class method to get the total number of students created.
        Uses cls to refer to the class itself.
        
        Returns:
            int: Total number of Student objects created
        """
        return cls.total_students
    
    def __str__(self):
        """
        String representation of the Student object.
        Called when the object is printed or converted to string.
        
        Returns:
            str: String representation
        """
        return f"Student('{self.name}', {self.roll_no})"
    
    def __repr__(self):
        """
        Official string representation for debugging.
        
        Returns:
            str: Detailed representation
        """
        return f"Student(name='{self.name}', roll_no='{self.roll_no}', department='{self.department}')"


# ============================================================================
# DEMONSTRATION OF CREATING MULTIPLE OBJECTS AND CALLING CLASS METHODS
# ============================================================================

def demonstrate_student_class():
    """
    Demonstration function showing how to create and use Student objects.
    """
    print("\n" + "="*70)
    print("DEMONSTRATION: STUDENT CLASS - OBJECT-ORIENTED PROGRAMMING")
    print("="*70)
    
    # Creating multiple Student objects
    print("\n1. Creating Student Objects...")
    print("-" * 70)
    
    student1 = Student(
        name="Muhammad Ahmed Khan",
        roll_no="CS101",
        department="Computer Science",
        email="ahmed.khan@paf-iast.edu.pk"
    )
    print(f"✓ Created: {student1}")
    
    student2 = Student(
        name="Fatima Zahra",
        roll_no="CS102",
        department="Computer Science",
        email="fatima.zahra@paf-iast.edu.pk"
    )
    print(f"✓ Created: {student2}")
    
    student3 = Student(
        name="Ali Hassan",
        roll_no="CS103",
        department="Computer Science",
        email="ali.hassan@paf-iast.edu.pk"
    )
    print(f"✓ Created: {student3}")
    
    # Display information for each student
    print("\n2. Displaying Student Information...")
    print("-" * 70)
    student1.display_info()
    student2.display_info()
    student3.display_info()
    
    # Demonstrating update_email method
    print("\n3. Updating Email Addresses...")
    print("-" * 70)
    student1.update_email("m.ahmed.khan@paf-iast.edu.pk")
    print()
    student2.update_email("f.zahra@paf-iast.edu.pk")
    
    # Displaying updated information
    print("\n4. Displaying Updated Information for Student 1...")
    print("-" * 70)
    student1.display_info()
    
    # Getting details as dictionary
    print("\n5. Getting Student Details as Dictionary...")
    print("-" * 70)
    student_dict = student3.get_details()
    print(f"Student 3 Dictionary: {student_dict}")
    
    # Using class method to get total students
    print("\n6. Getting Total Number of Students (Class Method)...")
    print("-" * 70)
    total = Student.get_total_students()
    print(f"Total Students Created: {total}")
    
    # Demonstrating __str__ method
    print("\n7. String Representation of Objects...")
    print("-" * 70)
    print(f"Student 1: {student1}")
    print(f"Student 2: {student2}")
    print(f"Student 3: {student3}")
    
    # Demonstrating __repr__ method
    print("\n8. Detailed Representation (for debugging)...")
    print("-" * 70)
    print(f"Student 1 repr: {repr(student1)}")
    print(f"Student 2 repr: {repr(student2)}")
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("="*70 + "\n")


# Run demonstration
if __name__ == "__main__":
    demonstrate_student_class()