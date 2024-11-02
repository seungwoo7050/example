class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def update_details(self, name=None, age=None):
        if name:
            self.name = name
        if age:
            self.age = age
            
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
# Dictionary to store student records
students = {}

def display_menu():
    print("\n--- Student Management System Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update a Student")
    print("4. Remove a Student")
    print("5. Exit")
    
def add_student():
    name = input("Enter student name: ")
    try:
        age = int(input("Enter student age: "))
        student_id = len(students) + 1
        students[student_id] = Student(name, age)
        print(f"Student added with ID: {student_id}")
    except ValueError:
        print("please enter a valid age.")
        
def view_students():
    if not students:
        print("No students in the system.")
    else:
        print("\n--- All Students ---")
        for student_id, student in students.items():
            print(f"ID: {student_id}, {student}")
            
def update_student():
    view_students()
    try:
        student_id = int(input("Enter student ID to update: "))
        if student_id in students:
            name = input("Enter new name (leave blank to keep current): ")
            age_input = int(input("Enter new age (leave blank to keep current): "))
            age = int(age_input) if age_input else None
            students[student_id].update_details(name=name or None, age=age)
            print("Student details updated.")
        else:
            print("Student ID not found.")
    except ValueError:
        print("Ivalid input. Please enter a valid ID and age.")

def remove_student():
    view_students()
    try:
        student_id = int(input("Enter student ID to remove: "))
        if student_id in students:
            removed_student = students.pop(student_id)
            print(f"Removed student: {removed_student}")
        else:
            print("Student ID not found.")
    except ValueError:
        print("Please enter a valid student ID.")
        
def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1, 5.")
    
if __name__ == "__main__":
    main()