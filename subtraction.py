"""subtraction of two numbers
requirement:result should always be positive"""


print(" ")
number1= int(input("please enter the first number:"))
number2= int(input("please enter the second number:"))
if number1>number2:
    print(" ")
    print("number1 is greater than number2 so:")
    print(f"the subtraction of {number1} and {number2} is:",number1-number2)
else:
    print(" ")
    print("number2 is greater than number1 so:")
    print(f"the subtraction of {number2} and {number1} is:",number2-number1)