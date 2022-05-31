#if_else_statements
#number = int(input("Enter the number to be evaluated :"))
#if number > 10:
#    print("The number is greater than 10")
#elif number < 10:
#    print("The number is not greater than 10")
#print("The End.")


#a= int(input("Enter number a :"))
#b=10
#if a<b:
#    print("a is less than b")
#elif a == b:
#    print("a is equal to b")
#elif a = b:
#    print("")
#else:
 #   print("a is greater than b")



#BMI
name = input("Enter your full names : ")
heightInMeters = int(input("Enter your height in Meters : "))
weightInKilograms = int(input("Enter your weight in Kilograms : "))
bmi = weightInKilograms / (heightInMeters ** 2)
print("Bmi of registered user: ",name , "is" , bmi)
if bmi >= 4:
    print("Sorry" , name,"." "You are overweight. Try again next time.")
else:
    print("Congratulations",name, "." "Welcome to the Kenya Defence Forces.")
print("\t")
print("Thankyou.")













