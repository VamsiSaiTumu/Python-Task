"""assignment 3-bug(login page)"""
""" in the line 7 basically input function take input as string by default  but passcode in line 5 which we have 
     entered is digit ,so to covert the string into digit we must use "int" to convert string to integer"""
user = "vamsi"
passcode = 12344
username = input("please enter the username:")
password = int(input("please enter your password:"))
if username == user and password == passcode:
   print(f"hello {username} welcome to python course:")
else:
    print("please enter correct username or password:")