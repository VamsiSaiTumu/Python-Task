"""Login page for 5 users using if,else,elif conditions"""
user1 = "vamsi"
user2 = "sai"
user3 = "sardar"
user4 = "king"
user5 = "singh"
passcode1 = "1234"
passcode2 = "4321"
passcode3 = "7890"
passcode4 = "0987"
passcode5 = "5678"
username = input("Please enter the username:")
if username == user1:
    password = input("Please enter the password:")
    if password == passcode1:
        print(f" Hi {username},welcome to the login page")
    else:
        print("Incorrect password,please enter correct password")
elif username == user2:
    password = input("Please enter the password:")
    if password == passcode2:
        print(f"Hi {username}, welcome to the login page")
    else:
        print("Incorrect password,please enter correct password")
elif username == user3:
    password = input("Please enter the password:")
    if password == passcode3:
        print(f"Hi {username}, welcome to the login page")
    else:
        print("Incorrect password,please enter correct password")
elif username == user4:
    password = input("Please enter the password:")
    if password == passcode4:
        print(f"Hi {username}, welcome to the login page ")
    else:
        print("Incorrect password,please enter correct password")
elif username == user5:
    password = input("Please enter the password:")
    if password == passcode5:
        print(f"Hi {username}, welcome to the login page")
    else:
        print("Incorrect password,please enter correct password")
else:
    print("Invalid username,please try again")
