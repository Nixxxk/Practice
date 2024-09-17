height = int(input("What is your height?"))
bill = 0

if height>=4:
    print("Can Ride? ")
    age = int(input("What is your age? "))
    if age<12:
        bill = 150
        print("Pay 150rs")
    elif age<=18:
        bill = 250
        print("pay 250rs")
    else:
        bill = 500
        print("pay 500rs")

    want_photo = input("Would you like to get photo printout?(Y/N) ")

    if want_photo == 'Y' or want_photo == 'y':
        bill = bill + 50
        print(f"Your total bill is {bill}.")
        
    else:
        print("Thankyou for using our services...!")
        
else:
    print("Can't Ride...!")
print("Bye..!")