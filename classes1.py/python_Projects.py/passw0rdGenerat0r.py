import random
print('Welcome to our password generator app! ')
print("\n")
enterChar = input('Enter your names: ')
num_passwords = int(input('How many passwords would you like to be generated: '))
lengthPasswords = int(input('Enter the length of the password: '))
print('Here are your passwords: ')
for pwd in range(num_passwords):
    passwords = ' '
    for c in range(lengthPasswords):
        passwords += random.choice(enterChar)
    print(passwords)



