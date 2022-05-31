#length test
password = str(input("Please enter your password: "))
if len(password) < 10:
    print("Sorry. Your password is too short. Try again")
else:
    password2 = str(input("Confirm your password: "))
    if password == password2:
        print("\t")
        print("Password input successfull")
        print("\n")
        print("Welcome to Instagram.")
    else:
        print("Your password does'nt align with the initial. Please try again.")
        






