rows = int(input("Enter the number of rows :"))
for i in range (0,rows+1):
    for j in range(0,rows-i+10):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")  
    print( "\t")