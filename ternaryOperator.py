#print("Welcome to Kenyatta University Eligibility Portal.")
#print("\n")
#full_names = str(input("Enter your full names: "))
#age = int(input("Enter your age :"))
#if age <= 17:
#    print("Sorry",full_names,"." "You are not eligible for our placement services.")
#elif age >= 24:
#    print("Sorry",full_names,"." "You are not eligible for our placement services.")
#kcse = int(input("Enter your KCSE mean grade points: "))
#if kcse <= 50:
#    print("Sorry",full_names,"." "You are not eligible for our placement services.")
#elif kcse >= 51:
#    str(input("Enter the name of your former highschool: "))
#gender = str(input("Enter your gender: "))
#if gender == "Male" or "male":
#    print("\t")
#    print("We will contact you soon",full_names,".")
#else:
#    str(input("Enter your phone number:"))

#ternartOperator
#print(input("Welcome to The Kenyatta University Placement Portal."))
#print("\t")
#full_names = str(input("Enter your full names: "))
#age = int(input("Enter your age :"))
#message = "Eligible" if age <= 18 else "Sorry.You are not Eligible."
#print(message)

#logicalOperators
#high_income = False
#male = True
#student = False 
#if (high_income or male) and not student:
#    print("Congratulations. Your are eligible.")
#else:
#   print("Sorry.Try again next time")

#chaining comparison Operators
#age = int(input("Enter your age: "))
#message = "Congratulations. You are eligible for the loan." if age >=18 and age <=65 else "Sorry. You are not eligible."
#print(message)

print("Welcome to our placement services")
print("\t")
full_names = str(input("Enter your full names: "))
residence = int(input("Enter your home postal address: "))
age = int(input("Enter your age: "))
if age >=18 and age <=60:
    print("Congratulations",full_names,".""You are eligible for our placement services.")
else:
    print("Sorry",full_names,".""You are not eligible for our placement services.")


   