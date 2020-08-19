import random

#  For loop explanation
#  used after defining the end condition, times of looping
#  3:29:52

#  Nested LOOP: FOR LOOP in WHILE LOOP
travelling = input('yes or no\n')

while travelling == 'yes':
    num = int(input('Number of travelling people:'))
    for num in range(1, num + 1):
        name = input('Name:')
        age = input('Age:')
        sex = input('Sex:')
        print(name)
        print(age)
        print(sex)
    travelling = input('Ooops! forgotten someone?')
#  _________________________________________________________________
#  exercise of printing pythagorean number a**2 + b**2 = c**2
from math import sqrt
n = int(input('Maximal Number: '))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c_square - c ** 2) == 0:
            print(a, b, c)
#  ________________________________________________________________
#  Example of NESTED WHILE LOOP
print('Welcome to IronBank of Mahama ATM')
restart = 'Y'
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter 4 Digit PIN: '))
    if pin == (1234):
        print('You entered the correct pin\n')
        while restart not in ('no', 'NO', 'n', 'N'):
            print('Please Press 1 for Your Balance\n')
            print('Please Press 2 to make a withdraw\n')
            print('Please Press 3 to pay in\n')
            print('Please Press 4 to Return your Card\n')
            option = int(input('What would like to choose?'))
            if option == 1:
                print('Your balance is $', balance, '\n')
                restart = input('Would you like to go back?')
                if restart in ('no', 'NO', 'n', 'N'):
                    print('Thank you!')
                    break
            elif option == 2:
                restart = 'y'
                withdraw = float(input('How much would you like to withdraw?\n $10? $20?'
                                       '$40? $60? $80? $100? I choose:  '))
                if withdraw in [10, 20, 40, 60, 80, 100]:
                    balance -= withdraw
                    print('\n Your balance is now $', balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('no', 'NO', 'n', 'N'):
                        print('Thank you!')
                        break
                elif withdraw != [10, 20, 40, 60, 80, 100]:
                    print(('Invalid Amount, Please retry\n'))
                    restart = ('y')
                elif withdraw == 1:
                    withdraw = float(input('Please enter desired amount: '))

            elif option == 3:
                Pay_in = float(input('How much would you like to pay in? '))
                balance += Pay_in
                print('\nYour balance is now $', balance)
                restart = input('Would you like to go back? ')
                if restart in ('no', 'NO', 'n', 'N'):
                    print('Thank you!')
                    break

            elif option == 4:
                print('Please wait whilst your card is returned...\n')
                print('Thank you for banking with us!')
                break

            else:
                print('Please enter a correct number. \n')
                restart = ('y')
    elif pin != (1234):
        print("Please enter a valid PIN")
        chances -= 1
        if chances == 0:
            print('\nNo more ties')
            break
#  _________________________________________________________




# __________________________________________________________
#  Example of FOR LOOP
fruits = ['Mangoes', 'Apples', 'Grapes']
for fruit in fruits:
    print('Current fruit is: ', fruit)

print('Goodbye!')

#  printing a factorial number by using for loop
num = int(input('Factorial Number: '))
factorial = 1

if num < 0:
    print('must be positive')
elif num == 0:
    print('factorial = 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print('Output', factorial)

# =================================================================================
# Random number
# Timer 3:29:00
# import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print('Number too large!')
        elif guess < to_be_guessed:
            print('Number too small')
    else:
        print('Sorry that you are giving up!')
        break
else:
    print('Congratulation. You made it!')

print()

print('Loops i python')
count = 1
while count <= 5:
    print(count)
    count += 1
print("You are done!")
print()
