def isLeapYear(year):
    return(year%4 == 0 and (year%100!=0 or year%400==0))

#y = int(input("Enter a year: "))
#isOrNot = isLeapYear(y)
#print(isOrNot)


def daysIn(year, month):
    assert 1<=month<=12     
    if month in [1, 3, 5, 7, 8, 10, 12]:
       print("31 days in this month")
    elif month == 2:
        if isLeapYear(year):
            print("29 days in this month")
        else:
            print("28 days in that month")
    else:
        print("30 days in this month")



month = int(input("Enter the month"))
year = int(input("Enter the year"))
days = daysIn(year, month)
print(days, "in this month")
