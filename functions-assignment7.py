print("calculator with functions")
#simple function
def add():
    print(f"addition of {x} and {y} is:",x+y)
#function with agrument and without return type
def sub(a,b):
    print(f"sustraction of {a} and {b}is:",a-b)
#function  without agrument with return type
def  mul():
     c= x*y
     return c
#function with agrument and return type
def div(a,b):
    c = a/b
    return c
#function with agrument and without return type
def mod(a,b):
    print(f"the division of {a} and {b} is:",a%b)
#function with agrument and return type
def pow(a,b):
    c=a**b
    return c
#function with agrument and return type
def floor(a=10,b=2):
    c=a//b
    return c
print("List of operations")
print("________________")
print("1.addition\n2.subtarction\n3.multiplication\n4.division\n5.reminder\n6.power\n7.floor division")
while True:
    print("---------------")
    choice = input("please enter operation to be performed:")
    if choice == '1':
        x = int(input("please enter the first number:"))
        y = int(input("please enter the second number:"))
        add()
        break
    elif choice =='2':
       x = int(input("please enter the first number:"))
       y = int(input("please enter the second number:"))
       sub(x,y)
       break
    elif choice =='3':
        x= int(input("please enter the first number:"))
        y= int(input("please enter the second number:"))
        print(f"multiplication of {x} and {y} is: ",mul())
        break
    elif choice =='4':
        x= int(input("please enter the first number:"))
        y = int(input("please enter the second number:"))
        print(div(x,y))
        break
    elif choice =='5':
        x = int(input("please enter the first number:"))
        y = int(input("please enter the second number:"))
        mod(x,y)
        break

    elif choice =='6':
         x = int(input("please enter the first number:"))
         y = int(input("please enter the second number:"))
         print(pow(x,y))
         break
    elif choice =='7':
         x = int(input("please enter the first number:"))
         y = int(input("please enter the second number:"))
         print(floor(x,y))
         break
    else:
        print("invalid choice ,please enter again")
        exit()
