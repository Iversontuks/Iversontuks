number = int(input("Enter the number :"))
factorial = 1
if number < 0 :
    print("factorial of number is less than zero")
elif number == 0 :
    print("factorial of 0 = 1")    
else :
    for number in range ( 1,number+1 )  :  
      factorial = factorial*number
print("factorial of number is :" , factorial)     


       
    
