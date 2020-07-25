'''list of 10 users with unique name'''
name=[]
for i in range(1,11):
    user=input(f"enter the name of the user {i}:")
    if user not in name:
        name.append(user)
        print(name)
    elif user in name:
        while user in name:
            print("the name is already taken")
            user =input("enter the another name:")
        if user not in name:
                name.append(user)
                print(name)
print("=================================================")
print("the data type is:",type(name))
print("the length of the list with unique names are :",len(name))
print(name)
