#ABMI/08305P/2023- MAGHANGA ROSINAH WAKIO
#BBIT PYTHON PROJECT
#EDUCATION SYSTEM

students = []

class Student:
    def __init__(self,student_ID, student_name, phone_number):
        self.student_ID = student_ID
        self.student_name = student_name
        self.phone_number = phone_number
        self.course = None
        self.fee = 0

    def display(self):
            print(f"ID: {self.student_ID}, Name: {self.student_name},Phone: {self.phone_number}")
            if self.course:
                print(f"Course: {self.course.course_name}, Fee: KES{self.fee}")

class Course:
    def __init__(self,course_name,fee):
        self.course_name = course_name
        self.fee = fee

    def discount(self):
            return 0 #default no discount

class Degree(Course):
    def discount(self):
        return 0.15 #15% discount for Degrees

class Diploma(Course):
    def discount(self):
        return 0.10 #10% discount for Diploma

class Certificate(Course):
    def discount(self):
        return 0.05 #5% discount for Certificates

class ShortCourse(Course):
    def discount(self):
        return 0  #No discount offered for Short Courses

#Payment Classes
class Payment:
    def pay(self,amount):
        pass

class MpesaPayment(Payment):
    def pay(self,amount):
        print(f"Payment of KES {amount} made via Mpesa.")

class CardPayment(Payment):
    def pay(self,amount):
        print(f"Payment of KES {amount} made via Card.")

class CashPayment(Payment):
    def pay(self,amount):
        print(f"Payment of KES {amount} made via Cash.")

class ChequePayment(Payment):
    def pay(self,amount):
        print(f"Payment of KES {amount} made via Bank Cheque.")

#HELPER FUNCTION
def get_student_by_ID(student_ID):
    for student in students:
        if student.student_ID == student_ID:
            return student
    return None

#This section adds new student records
def add_student():
    student_ID = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    phone_number = input("Enter phone number: ")

    students.append(Student(student_ID, student_name, phone_number))
    print("Student added successfully.")

#To view all student records
def view_students():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            student.display()

#Search for student using Student ID
def search_student():
    search_ID = input("Enter student ID to search: ")
    student = get_student_by_ID(search_ID)
    if student:
        student.display()
    else:
        print("Student not found.")

#Update a Student's phone number
def update_student():
    search_ID = input("Enter student ID to update: ")
    student = get_student_by_ID(search_ID)
    if student:
         new_phone_number = input("Enter new phone number: ")
         student.phone_number = new_phone_number
         print("Student record updated successfully.")
    else:
        print("Student not found.")

#Course selection and payment
def select_course():
    student_ID = input("Enter student ID for course enrollment: ")
    student = get_student_by_ID(student_ID)

    if not student:
        print("Student not found. Please add student first.")
        return

    courses = {
        1: Degree("Degree Program", 120000),
        2: Diploma("Diploma Program", 60000),
        3: Certificate("Certificate Program", 30000),
        4: ShortCourse("ShortCourse Program", 15000)
    }
    print("\n AVAILABLE COURSES")
    for key, course in courses.items():
        print(f"{key}. {course.course_name} - KES {course.fee}")

    choice = int(input("Select a course: "))
    selected_course = courses.get(choice)

    if not selected_course:
            print("Course not found.")
            return

    discount_rate = selected_course.discount()
    discount_amount = selected_course.fee * discount_rate
    total_fee = selected_course.fee - discount_amount

    student.course = selected_course
    student.fee = total_fee

    print("\nFEE DETAILS")
    print("Course Selected: ", selected_course.course_name)
    print("Original Fee: ", selected_course.fee)
    print("Discount: ", discount_rate)
    print("Total Payable: KES ", total_fee)

    print("\nSelect payment Method")
    print("1. Mpesa")
    print("2. Card")
    print("3. Cash")
    print("4. Bank Cheque")

    pay_choice =input("Input Choice for Payment: ")
    if pay_choice == "1":
        payment = MpesaPayment()
    elif pay_choice == "2":
        payment = CardPayment()
    elif pay_choice == "3":
        payment = CashPayment()
    elif pay_choice == "4":
        payment = ChequePayment()
    else:
        print("Invalid Choice.")
        return

    payment.pay(total_fee)
    print("Enrollment Completed Successfully.")

#MAIN MENU
def main_menu():
    while True:
        print("\nEDUCATION MANAGEMENT SYSTEM")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Record")
        print("5. Select Course & Make Payment")
        print("6. Exit")

        choice= input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            select_course()
        elif choice == "6":
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

main_menu()


