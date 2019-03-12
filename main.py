##################################################################
# Pybank Assigment
# Date 3/11/2019
# Sanjay Mamidi
# Data Viz Class
#################################################################

import os
import csv

# path = 'c/Users/rekhapc/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyBank/Resources'
csvpath = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python', 'Homework', \
                       'Instruction', 'PyBank', 'Resources', 'budget_data.csv')
fileToWite = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python',  \
                    'python-challenge', 'PyBank',  'pybankout.txt')

totalMonths = 0
money = 0
average = 0
moneyCurrentMonth = 0
moneyPriorMonth = 0
increaseInMoney = 0
decreaseInMoney = 0
highIncreaseInMoney = 0
highDecreaseInMoney = 0
moneydate = ()  # tuple
averageChange = 0
moneyChangeMonthly = []  # store (money, date) tuple ie -$250,Jan 2014

def aveFunction(List):
    sumOfNumbers = sum([i[0] for i in List])
    return (sumOfNumbers / len(List))

file = open(fileToWite,"w")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', )
    next(csvreader)
    for row in csvreader:
        totalMonths += 1
        date = row[0]
        money = int(row[1]) + money
        moneyCurrentMonth = int(row[1])

        # do magnitude of change processing
        # print(f'moneycurrentmonth is {moneyCurrentMonth}')
        # print(f'moneypriormonh is {moneyPriorMonth}')
        # print(f'date {date}')
        if moneyCurrentMonth > 0:  # ie positive amt
            if moneyPriorMonth > 0:  # also postive amount
                if moneyCurrentMonth > moneyPriorMonth:  # +ve cash this month and last month & net change is +ve
                    increaseInMoney = moneyCurrentMonth - moneyPriorMonth
                    moneydate = (increaseInMoney, date)
                    moneyChangeMonthly.append(moneydate)  # add to monthly list
                elif moneyCurrentMonth < moneyPriorMonth:  # net change is -ve but > 0
                    decreaseInMoney = moneyCurrentMonth - moneyPriorMonth  # will be a -ve amount
                    moneydate = (decreaseInMoney, date)
                    moneyChangeMonthly.append(moneydate)  # add to monthly list
            elif moneyPriorMonth < 0:  # -ve amount but net change will be positive since money this month is +ve
                # print(f'moneypriormonth is {moneypriormonth} and current month is {moneyCurrentMonth}')
                increaseInMoney = ((moneyPriorMonth) * (-1)) + moneyCurrentMonth  # erased the deficiet and then some
                # print(f'increase in money is {increaseInMoney}')
                moneydate = (increaseInMoney, date)
                moneyChangeMonthly.append(moneydate)  # add to monthly list
                # swing in profits from -ve last month to +ve this month
        elif moneyCurrentMonth < 0:  # -ve amount
            if moneyPriorMonth > 0:  # also postive amount
                # swing in netmoney is -ve and is total of  money for this month + the magnitude of loss for prior month
                decreaseInMoney = -1 * (((-1) * (moneyCurrentMonth)) + moneyPriorMonth)
                moneydate = (decreaseInMoney, date)
                moneyChangeMonthly.append(moneydate)
            elif moneyPriorMonth < 0:  # negative amount
                # both negative so net swing is also negative
                if (-1) * (moneyCurrentMonth) > (-1) * (moneyPriorMonth):  # loss this month is > loss prior month
                    decreaseInMoney = (-1) * ((-1) * (moneyCurrentMonth) - (-1) * (moneyPriorMonth))
                    moneydate = (decreaseInMoney, date)
                    moneyChangeMonthly.append(moneydate)
                elif (-1) * (moneyCurrentMonth) < (-1) * (moneyPriorMonth):
                    # loss this month is < loss last month
                    decreaseInMoney = (-1) * ((-1) * (moneyPriorMonth) - (-1) * (moneyCurrentMonth))
                    moneydate = (decreaseInMoney, date)
                    moneyChangeMonthly.append(moneydate)

        # finally reset the current and proir monthvariables
        moneyPriorMonth = moneyCurrentMonth
    averageChange = aveFunction(moneyChangeMonthly)


#tostdout
print(f'Total Months: {totalMonths}')
print(f'Total: ${money}')
moneyChangeMonthly.sort()
print(f'Greatest Decrease  {moneyChangeMonthly[0:1]}')
moneyChangeMonthly.sort(reverse=True)
print(f'Greatest Increase  {moneyChangeMonthly[0:1]}')
print(f'Average Change   = ${averageChange}')

#tofile
file.write(f'Total Months: {totalMonths} \n')
file.write(f'Total: ${money} \n')
file.write(f'Greatest Increase  {moneyChangeMonthly[0:1]} \n')
moneyChangeMonthly.sort()
file.write(f'Greatest Decrease  {moneyChangeMonthly[0:1]} \n')
file.write(f'Average Change   = ${averageChange} \n')
file.close()