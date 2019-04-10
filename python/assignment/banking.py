import re
import os


def accountcreation():
    
    username=input("Enter your username: ")
    password=input("Enter your password: ") 
    
    with open('Login.txt', 'a') as file:
        file.writelines(username + "," + password + "\n")

    with open('Accountbook.txt', 'a') as file:
        file.writelines(username +",0"+"\n")
    os.system('cls')  # on windows

def login(supplied_username,supplied_password):
    os.system('cls')  # on windows
    loggedin= False
    pattern = "^"+supplied_username+","+supplied_password+"$"
    file = open("Login.txt","r")
    for line in file.readlines():
        if re.search(pattern, line, re.I):
            loggedin= True
            break
    if(loggedin==True):
        print("You are Logged in!")
        useroptions(supplied_username)

    else:
        print("Login First!")    
    file.close()    


def useroptions(supplied_username):
    os.system('cls')  # on windows

    print("Hello!",supplied_username,"welcome to our bank enter what u want to do with your account!")
    print("Enter 1 to Withdraw")
    print("Enter 2 to Deposit")
    print("Enter 3 to Check Balance")
    print("Enter 4 to Delete Account")

    option=int(input("Option Number?: "))

    if(option == 1):
        withdraw(supplied_username)
    elif (option == 2):
        deposit(supplied_username)
    elif (option == 3):
        display(supplied_username)
    elif (option == 4):
        delete(supplied_username)    

def  delete(supplied_username):
    pattern =  "^"+supplied_username+",-?\d*\.{0,1}\d+$"
    file = open("Accountbook.txt","r+")
    for line in file.readlines():
        if re.search(pattern, line, re.I):
            f = open("yourfile.txt","r")
            lines = f.readlines()
            f.close()
            for line in lines:
                if line!="nickname_to_delete"+"\n":
                    f.write(line)


def withdraw(supplied_username):

    os.system('cls')  # on windows

    balance = 0
    withdraw_amount = int(input("Enter the amount you want to withdraw:"))
    pattern =  "^"+supplied_username+",-?\d*\.{0,1}\d+$"
    file = open("Accountbook.txt","r+")
    for line in file.readlines():
        if re.search(pattern, line, re.I):
            lst = line.split(',')
            value = lst[1]
            balance = int(value[:-1])
            amountleft = balance-withdraw_amount
            print(amountleft)
            data = open("Accountbook.txt").read()
            file.seek(0)
            file.write(re.sub(supplied_username+","+str(balance),supplied_username+","+str(amountleft),data))
            file.close()
            break        
    print("Do you want to continue? Press 1 if yes and 2 if no")
    option=int(input("Option Number? "))
    if(option == 1):
        useroptions(supplied_username)
    
def deposit(supplied_username):
    os.system('cls')  # on windows

    deposit_amount = int(input("Enter the amount you want to deposit:"))
    pattern =  "^"+supplied_username+",-?\d*\.{0,1}\d+$"
    file = open("Accountbook.txt","r+")
    for line in file.readlines():
        if re.search(pattern, line, re.I):
            lst = line.split(',')
            value = lst[1]
            balance = int(value[:-1])
            amountleft = balance+deposit_amount
            print(amountleft)
            data = open("Accountbook.txt").read()
            file.seek(0)
            file.write(re.sub(supplied_username+","+str(balance),supplied_username+","+str(amountleft),data))
            file.close()
            break   
    print("Do you want to continue? Press 1 if yes and 2 if no")
    option=int(input("Option Number? "))
    if(option == 1):
        useroptions(supplied_username)
            

def display(supplied_username):
    os.system('cls')  # on windows

    pattern = "^"+supplied_username+",-?\d*\.{0,1}\d+$"
    file = open("Accountbook.txt","r")
    for line in file.readlines():
        if re.search(pattern, line, re.I):
            lst = line.split(',')
            balance = lst[1]
            print("Rs. ",balance)
            break
    print("Do you want to continue? Press 1 if yes and 2 if no")
    option=int(input("Option Number? "))
    if(option == 1):
        useroptions(supplied_username)
            

def ListUsers():
    os.system('cls')  # on windows

    count = 1
    file = open("Login.txt","r")
    lines = file.readlines()
    for line in lines:
        lst = line.split(',')
        username = lst[0]
        print(count ,": ",username)
        count = count+1
    print("Do you want to exit? Press 1")
    option=int(input("Option Number? "))       

x=1
while(x>0):
    os.system('cls')  # on windows
    print("Welcome to our virtual banking system!")
    print("Enter 1 to login")
    print("Enter 2 to create account.")
    print("Enter 3 for User List")
    
    option=int(input("Option Number? "))
    os.system('cls') 

    if(option == 1):
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        login(username,password)
        
    elif (option == 2):
        accountcreation()

    elif (option == 3):
         ListUsers()


