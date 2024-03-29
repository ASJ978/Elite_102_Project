import mysql.connector
conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306)

userName = ""
pwd = ""
##Welcome message

print("Hello! Welcome to the bank!\n")

###Check if need to make account
acctCreate = input("Are you new to this bank? y/n: ")

###If need to make account, create username and password
if acctCreate == "y":
    userName = input("Please provide a username: ")
    pwd = input("Please provide a password: ")
    
###If not need to make account used previous stored username and pwd
if acctCreate == "n":
    checkName = input("Please enter your username: ")
    checkPwd = input("Please enter your pwd: ")