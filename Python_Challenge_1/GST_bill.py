"""
Write a function which takes in user’s restaurant bill
and provide GST (18%) and return the total.Also
Include 20% tip as service if user wishes to pay
Steps
takes in one Argument (users_restaurant_ bill)
Add 18% GST and add to the the Bill.
If users wishes to pay the service TAX add 20%
amount else don’t add 20% amount
"""
# Taking bill amount
users_restaurant_bill = float(input("Enter the bill amount"))
total_bill = 0.0
gst = 0.18
tip = 0.2


def billing(bill):
    global total_bill

    # Adding GST
    total_bill = bill + bill * gst
    print("Your bill was Rs.", bill, "\nAfter adding GST it is now Rs.", total_bill)

    # Asking if the customer wants to tip
    tip_ask = input("Would you like to tip our waiters\nAnswer in yes or no")
    tip_ask.casefold()
    if tip_ask == "yes":
        total_bill += bill * tip

    # Printing final bill
    print("Your total bill is Rs.", total_bill)
    print("Thank you for eating")


billing(users_restaurant_bill)
