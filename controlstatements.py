temperature = float(input("Enter temperature "))

if temperature > 25:
    print("It is too hot")

else:
    print("It is too cold")

#python program that checks three numbers and returns the smallest
num1=int(input("Enter Num1: "))
num2=int(input("Enter Num2: "))
num3=int(input("Enter Num3: "))


if num1<num2 and num1<num3:
    print(num1 ,"is the smallest")
elif num1 < num2 and num2< num3:
    print(num2,"is the smallest")
else:
    print(num3,"is the smallest")

# program to check whether a number even or odd
number=int(input("Enter number"))
if number %2 ==0:
    print(number,"is an even number")
else:
    print(number,"is an odd number")