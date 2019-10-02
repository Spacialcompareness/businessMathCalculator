#! python3
#busMatCal.py is a Simple Interest Calculator for Business Mathematics

import time
selection = int(0)

options = {'Interest Total': '1.', 'Rate': '2.',
           'Time': '3.', 'Principal': '4.'}

#These are instructions.
print('Simple Interest Calculator'.center(40, '-'))
print('\nWhat can we help you find?'.center(40, ' '))
print('\nFirst, a few instructions.')

print('After each equation you will be brought back to the menu.\n' 
        'From the main menu you can exit by pressing \'000\'. You have to get to the menu before you can exit.\n'
        'Do not enter any special characters, digits only. No dollar signs, commas, or % sigs.\n'
        'Press \'999\' from the menu to exit.')

#FUNCTIONS

def getPrincipal():
    principal = input(("Principal: Digits only. "))
    return principal

def getInterest():
    interest = input("Interest: Digits only. ")
    return interest

def getRate():
    rat = input("Interest rate per annum: Digits only. ")
    return rat

def getTime():
    gettim = input("Is time in days(d), months(m) or years(y)? ")
    if gettim == 'd':
        tim = (int(input('How many days(d)? ')) / 365)
        #gettim = int(input() / 365)
        return tim
    elif gettim == 'm':
        tim = (int(input('How many months(m)? ')) / 12)
        #gettim = int(input() / 12)
        return tim
    elif gettim == 'y':
        tim = input('How many years(y)? ')
        #gettim = input()
        return tim
    else: #TODO this does not work.
        print('Not a valid option. Please select \'d\', \'m\', or \'y\'.')

def simIntTot(): #This function finds the interest total in a simple interest calculation.
    prin = int(getPrincipal())
    rate = (float(getRate()) / int(100))
    time = int(getTime())

    total = (prin * (1 + (rate * time)))
    interest = ((prin * (1 + (rate * time))) - prin)
    print('The total is ${0:,.2f}.' .format(total))
    print('The interest is ${0:,.2f}.'.format(interest))

def simIntRat(): #This function finds the rate in a simple interest calculation.
    prin = int(getPrincipal())
    inte = int(getInterest())
    time = float(getTime())

    rate = ((100 * inte) / (prin * time))
    print('The rate is {0:,.4f}%.' .format(rate))

#TODO Refactor
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

#TODO Refactor
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
    print('\nYou are at the main menu. What would you like to find?\n'
          '\'999\' to exit.')

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
