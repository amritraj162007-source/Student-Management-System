students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Course": course}
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No student records found.")
    for roll, details in students.items():
        print(roll, details)

def search_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student Not Found")

def delete_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        del students[roll]
        print("Record Deleted!")
    else:
        print("Student Not Found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
