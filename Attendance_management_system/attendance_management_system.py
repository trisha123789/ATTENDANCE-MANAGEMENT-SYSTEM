#----------------ATTENDANCE MANAGEMENT SYSTEM --------------------------------------------------
import database
database.create_table()

welcome = "WELCOME TO ATTENDANCE MANAGEMENT SYSTEM 📘"
print(welcome)
menu = """
1. ADD STUDENT
2. MARK ATTENDANCE
3.VIEW ATTENDANCE
4.SUMMARY
5.EXIT
"""


while (user_input := input(menu)) != "5":
    if user_input == "1":
        name = input("ENTER THE NAME OF THE STUDENT : ")
        database.add_student(name)
        print(F"STUDENT : {name} ADDED SUCCESSFULLY")


    elif user_input == "2":
        student_id = int(input("ENTER THE STUDENT ID  :"))
        status = input("PRESENT OR ABSENT (y or n)").lower() == 'y'
        database.mark_attendance(student_id,status)
        print("ATTENDANCE MARKED SUCCESSFULLY")


    elif user_input == "3":
        student_id = int(input("ENTER THE STUDENT ID:"))
        database.view_attendance(student_id)

    elif user_input == "4":
        print("-------------📊SUMMARY--------------")
        database.summary()
    else:
        print("INVALID  INPUT")


