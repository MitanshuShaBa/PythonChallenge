'''
Write a Function to check User’s Passwords.If
Password matches print welcome user else print
access denied

Steps:
-Function takes in 2 arguments (correct
Password,User Entered password):
-If user Password and Password entered is equal -
Welcome the User
-Deny the Access
'''

cor_pass = ""
user_pass = ""
num = 2


# Taking the correct password
def correctpass():
    global cor_pass
    cor_pass = input("Please enter correct password")


correctpass()


# Taking the user input password
def take_input():
    global user_pass
    user_pass = input("Please enter your password")


take_input()


# Checking password
def pass_check(cp, up):
    global num

    # checks if user input password is equal to correct password
    if cp == up:
        print("Welcome")
        quit()
    else:

        # giving more chances to try
        if num == 0:
            print("Too many failed attempts\nPlease try again after some time")
            quit()
        print("You have", num, "chances left.")

        num -= 1
        take_input()
        pass_check(cor_pass, user_pass)


pass_check(cor_pass, user_pass)
