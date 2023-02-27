import random
import sys, os

def sub(number3):
    subt = int(targetNumber - number3)
    if subt<9 and subt>-9:
        return 1
    else:
        return 0

numbers = list()
numbers.append(random.randint(10,99))
targetNumber = random.randint(100,999)

for i in range(5):
    numbers.append(random.randint(0,10))
while True:
    print(numbers)
    print("Target Number : ",targetNumber)
    print("Please First Choose Bigger Number\n")
    print("Please Enter Which Number Would You Use : \n")
    number1 = int(input())
    print("This list does not contain this number")& sys.exit(1) if number1 not in numbers else print("Good One")
    print("Please Enter Which Number Would You Use : \n")
    number2 = int(input())
    print("This list does not contain this number")& sys.exit(1) if number2 not in numbers else print("Good One")

    print("1 - Sum of {} and {} is {}".format(number1,number2,number1+number2))
    print("2 - Subtract of {} and {} is {}".format(number1,number2,number1-number2))
    print("3 - Multiplication of {} and {} is {}".format(number1,number2,number1*number2))
    print("4 - {} Divided by {} is {}".format(number1,number2,number1/number2))
    print("If you want to continue without create any numbers , just key 5 \n")


    print("Which one you want to use ?")
    Choice = int(input())
    match Choice:
        case 1:
            numbers.append(number1+number2)
            print(numbers)
        case 2:
            numbers.append(number1-number2)
            print(numbers)
        case 3:
            numbers.append(number1*number2)
            print(numbers)
        case 4:
            numbers.append(number1/number2)
            print(numbers)
        case 5:
            break

print(numbers)
print("What is the closest number you can reach the target number ?")
number3 = int(input())
result = sub(number3)
print("Congrats") if result == 1 else print("Sorry")