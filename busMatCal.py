#! python3
#busMatCal.py is a Simple Interest Calculator for Business Mathematics

import time
selection = int(0)

options = {'Interest Total': '1.', 'Rate': '2.',
           'Time': '3.', 'Principal': '4.'}

#These are instructions.
print('Simple Interest Calculator'.center(40, '-'))
print('\nWhat can we help you find?\n'.center(40, ' '))
#time.sleep(1.5) uncomment to put a time delay
print('First, a few instructions.')
#time.sleep(1.5) uncomment to put a time delay
print('After each equation you will be brought back to the menu.\n' 
        'From the main menu you can exit by pressing \'000\'. You have to get to the menu before you can exit.')
#time.sleep(1.5) uncomment to put a time delay
print('Do not enter any special characters, digits only. No dollar signs, commas, or % sigs.')
#time.sleep(2.5) uncomment to put a time delay
print('Press \'999\' from the menu to exit.')

#FUNCTIONS

def simIntTot(): #This function finds the interest total in a simple interest calculation.
    print("Principal: Digits only.")
    principal = int(input())
    print("Interest rate per annum? Digits only. ")
    rate = (float(input()) / 100)
    print('Is time in days(d) or months(m)? ')
    time = input()
    if time == 'd':
        print('How many days? ')
        time = (int(input()) / 365)

    else:
        print('How many months? ')
        time = (int(input()) / 12)

    total = (principal * (1 + (rate * time)))
    interest = ((principal * (1 + (rate * time))) - principal)
    print('The total is ${0:,.2f}.' .format(total))
    print('The interest is ${0:,.2f}.'.format(interest))
    #time.sleep(2)

def simIntRat(): #This function finds the rate in a simple interest calculation.
    print("Principal: Digits only.")
    principal = int(input())
    print("Total interest: Digits only. ")
    interest = float(input())
    print('Is time in days(d) or months(m)? ')
    time = input()
    if time == 'd':
        print('How many days? ')
        time = (int(input()) / 365)

    else:
        print('How many months? ')
        time = (int(input()) / 12)

    rate = ((100 * interest) / (principal * time))

    print('The rate is {0:,.4f}%.' .format(rate))

def simIntTim(): #This function finds the time in a simple interest calculation.
    print("Principal: Digits only.")
    principal = int(input())
    print("Total interest: Digits only. ")
    interest = float(input())
    print("Interest rate per annum? Digits only. ")
    rate = (float(input()) / 100)
    print('Do you want to see time in days(d), months(m) or years(y)? ')
    timeVar = input()
    if timeVar == 'd':
        timeVar = 365
        timUni = 'days'

    elif timeVar == 'm':
        timeVar = 12
        timUni = 'months'

    else:
        timeVar = 1
        timUni = 'years'

    time = (interest / (principal * rate) * timeVar)

    print('The time is {0:,.2f}'.format(time) + ' ' + str(timUni))
    #time.sleep(2)

def simIntPrin(): # This function finds the principal in a simple interest calculation.
    print("Total interest: Digits only. ")
    interest = float(input())
    print("Interest rate per annum? Digits only. ")
    rate = (float(input()) / 100)
    print('Is in days(d), months(m) or years(y)? ')
    time = input()
    if time == 'd':
        print('How many days? ')
        time = (int(input()) / 365)

    elif time == 'm':
        print('How many months? ')
        time = (int(input()) / 12)

    else:
        print('How many years?')
        time = int(input())

    principal = (interest / (rate * time))

    print('The principal amount is ${0:,.2f}.'.format(principal))
    #time.sleep(2)
    #print('The interest is ${0:,.2f}.'.format(interest))

while selection != 999:
    print('\nYou are at the main menu. What would you like to find? ')

    def optionsFunc(optionAlign, leftWidth, rightWidth):
        for k, v in optionAlign.items():
            print(str(v).ljust(leftWidth, '_') + k.rjust(rightWidth, '_'))
        print('\n')
    optionsFunc(options, 20, 20)

    selection = int(input())

    if selection == 1:
        simIntTot()

    elif selection == 2:
        simIntRat()

    elif selection == 3:
        simIntTim()

    elif selection == 4:
        simIntPrin()

    elif selection == 000:
        break

    else:
        print('Please make a valid selection.')
