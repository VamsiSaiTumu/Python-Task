'''list-program to check the amount of the user after entering the id'''
name= ["aman","preet","singh"]
id = ['147','258','369']
amount=['1400','2000','6500']
userid = input("please enter your id:")
try:
    for i in range(10000):
        if userid in id:
            if userid ==id[i]:
                print(f"Hi {name[i]},your amount balance is:{amount[i]}")
    if userid not in id:
        print("please check the id and re-enter")
except:
    pass