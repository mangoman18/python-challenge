##################################################################
# Pybank Assigment
# Date 3/11/2019
# Sanjay Mamidi
# Data Viz Class
# Creates one for loop to go thru the calculation of money change from
# month to month.
# Calculates Change in Money via a function that simply returns the difference
# between prior and current month money .
# Also calculates Avg Change via an function that sums all changes(+ve and -ve) per month
# and divides by total number of months
#################################################################

import os
import csv

totalMonths = 0
money = 0
average = 0
moneyCurrentMonth = 0
moneyPriorMonth = 0
increaseInMoney = 0
decreaseInMoney = 0
moneyDate = ()  # tuple
averageChange = 0
moneyChangeMonthly = []  # store (money, date) tuple ie -$250,Jan 2014
rowcnt = 0
# path = 'c/Users/rekhapc/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyBank/Resources'
csvpath = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python', 'Homework', \
                       'Instruction', 'PyBank', 'Resources', 'budget_data.csv')
fileToWite = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python', \
                          'python-challenge', 'PyBank',  'pybankout.txt')

file = open(fileToWite,"w")

def avgfunction(moneyDateListIn):
    sumOfNumbers = sum([mnthlymoney[0] for mnthlymoney in moneyDateListIn])
    return sumOfNumbers / len(moneyDateListIn)


def changepermonth(moneyCurrentMonthIn, moneyPriorMonthIn):
    return moneyCurrentMonthIn - moneyPriorMonthIn


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', )
    next(csvreader)
    for row in csvreader:
        totalMonths += 1
        date = row[0]
        money = int(row[1]) + money
        moneyCurrentMonth = int(row[1])
        rowcnt += 1
        #  do magnitude of change processing
        # except for first row since there is no history to compare with
        if rowcnt > 1:
            moneyDate = (changepermonth(moneyCurrentMonth,moneyPriorMonth), date)
            moneyChangeMonthly.append(moneyDate)  # add to monthly list

        # finally reset the current and prior month variables
        moneyPriorMonth = moneyCurrentMonth

    # Now Calc the avg money change between month to month
    averageChange = avgfunction(moneyChangeMonthly)

# to stdout
print(f'Total Months: {totalMonths}')
print(f'Total: ${money}')
print(f'Average Change: ${round(averageChange,2)}')
moneyChangeMonthly.sort(reverse=True)
print(f'Greatest Increase in Profits {moneyChangeMonthly[0:1][0][1]} (${moneyChangeMonthly[0:1][0][0]})')
moneyChangeMonthly.sort()
print(f'Greatest Decrease in Profits {moneyChangeMonthly[0:1][0][1]} (${moneyChangeMonthly[0:1][0][0]})')

# to file
file.write(f'Total Months: {totalMonths}\n')
file.write(f'Total: ${money}\n')
file.write(f'Average Change: ${round(averageChange,2)}\n')
moneyChangeMonthly.sort(reverse=True)
file.write(f'Greatest Increase in Profits {moneyChangeMonthly[0:1][0][1]} (${moneyChangeMonthly[0:1][0][0]})\n')
moneyChangeMonthly.sort()
file.write(f'Greatest Decrease in Profits {moneyChangeMonthly[0:1][0][1]} (${moneyChangeMonthly[0:1][0][0]})')
