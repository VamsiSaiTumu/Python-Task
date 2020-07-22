"""simple calculator"""
print("select 1 for addition:")
print("select 2 for subtraction")
print("select 3 for multiplication")
print("select 4 for division")
print("select 5 to get power of two numbers")
print("select 6 to get the remainder of two number")
print("select 7 to get module division of two numbers")
print("====================================================")
choice = input("the select the number to perform required operation:")
while True:
    if choice =="1":
        number1=int(input("please enter number1:"))
        number2=int(input("please enter number2:"))
        result=number1 + number2
        print(f"the sum of {number1} and {number2} is",result)
        break
    elif choice == "2":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 - number2
        print(f"the difference of {number1} and {number2} is", result)
        break
    elif choice == "3":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 * number2
        print(f"the multiplication of {number1} and {number2} is", result)
        break
    elif choice == "4":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 / number2
        print(f"the division of {number1} and {number2} is", result)
        break
    elif choice == "5":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 ** number2
        print(f"the power of {number1} and {number2} is", result)
        break
    elif choice == "6":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 % number2
        print(f"the remainder of {number1} and {number2} is", result)
        break
    elif choice == "7":
        number1 = int(input("please enter number1:"))
        number2 = int(input("please enter number2:"))
        result = number1 // number2
        print(f"the modulo division  of {number1} and {number2} is", result)
        break
    else:
        print("\ninvalid choice,please select the required from 1 to 7 ")
        exit()