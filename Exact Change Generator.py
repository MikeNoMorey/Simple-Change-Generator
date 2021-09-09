#Created by: Mike Morey
#Simple Change Generator v1.0
#***Works mainly with integers***
#Thanks for looking :)
print('Please input the amount of money recieved:')
total_change = int(input())
print()

if total_change <= 0:
    print('No change')

dollars = total_change // 100
total_change = total_change % 100

if dollars > 0:
    print(dollars, 'Dollars')
elif dollars == 1:
    print(dollars, 'Dollar')

quarters = total_change // 25
total_change = total_change % 25

if quarters > 0:
    if quarters == 1:
        print(quarters, 'Quarter')
    else:
        print(quarters, 'Quarters')
        
dimes = total_change // 10
total_change = total_change % 10
        
if dimes > 0:
    if dimes == 1:
        print(dimes, 'Dime')
    else:
        print(dimes, 'Dimes')
    
nickels = total_change // 5
total_change = total_change % 5
        
if nickels > 0:
    if nickels == 1:
        print(nickels, 'Nickel')
    else:
        print(nickels, 'Nickels')
        
           
pennies = total_change // 1
total_change = total_change % 1         
           
if pennies > 0:
    if pennies == 1:
        print(pennies, 'Penny')
    else:
        print(pennies, 'Pennies')
print()
print('Have a good one!')


