# Student Registration System

students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[student_id] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No students registered.")
        return

    print("\n--- Student List ---")
    for sid, details in students.items():
        print(f"ID: {sid}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Course: {details['Course']}")
        print("-------------------")

def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        s = students[student_id]
        print("\n Student Found")
        print(f"Name: {s['Name']}")
        print(f"Age: {s['Age']}")
        print(f"Course: {s['Course']}")
    else:
        print("Student not found!")

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student not found!")
        return

    print("Enter new details (leave blank to keep old value)")
    name = input("New Name: ")
    age = input("New Age: ")
    course = input("New Course: ")

    if name:
        students[student_id]["Name"] = name
    if age:
        students[student_id]["Age"] = age
    if course:
        students[student_id]["Course"] = course

    print("Student details updated!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def main_menu():
    while True:
        print("\n====== Student Registration System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
main_menu()
