#The Greatest Showdown

#Task 1: Identify the Greatest
#Task 2: Identify the Smallest

print("Enter three numbers and I will tell you which number is the largest and which is the smallest. ")

num1 = input("1st number: ")
num2 = input("2nd number: ")
num3 = input("3rd number: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
elif num3 > num1 and num3 > num2:
    print(num3, "is the largest number")


if num1 < num2 and num1 < num3:
    print("and ", num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print("and ", num2, "is the smallest number")
elif num3 < num1 and num3 < num2:
    print("and ", num3, "is the smallest number")