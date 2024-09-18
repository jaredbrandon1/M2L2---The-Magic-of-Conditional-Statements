#Leap Year Explorer

#Task 1. Leap Year Checker

year = input("Type a year to find out if it is or is not a leap year. ")
year = int(year)


if year % 4 == 0 and year % 400 ==0 :
    print(year, "is a leap year! ")
elif year % 4 == 0 and year % 100 ==0 :
    print(year, "is not leap year! ")
elif year % 4 == 0:
    print(year, "is a leap year! ")
else:
    print(year, "is not a leap year!")