# Write a function to check whether users Attendance is greater than or equal to 75%.
# If greater than 75% student can sit for Unit Test examination or student is not allowed to sit for the examination.
# Steps:Takes in the student attendance in the function as the argument.Use if-else

print("Welcome")


# Takes input for attendance
def take_input():
    global attend
    attend = input("Please enter your attendance% \n")


take_input()


def admittance(x):
    # Restricts input of wrong attendance
    if int(x) < 0:
        print("Enter the attendance properly")
        take_input()
        admittance(attend)
        quit()
    if int(x) > 100:
        print("Enter the attendance properly")
        take_input()
        admittance(attend)
        quit()

    # Checks the atttendance
    else:
        if int(x) >= 75:
            print("You are eligible to write the Unit Test")
        else:
            print("You are not eligible to write the Unit Test")


admittance(attend)
