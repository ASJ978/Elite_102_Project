import mysql.connector
conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306, database = "bank_data")
cursor = conn.cursor()

add_data = "INSERT INTO user_info (userName, pwd) VALUES(%s, %s)"
##conn.close()





userName = ""
pwd = ""
##Welcome message
def main():
    print("Hello! Welcome to the bank!\n")
    acctCreate = input("Are you new to this bank? y/n: ")
 ###Check if need to make account   
    if acctCreate == "y":
        newAccnt()
    if acctCreate == "n":
        prevAccnt()




###If need to make account, create username and password
def newAccnt():
    userName = input("Please provide a username: ")
    pwd = input("Please provide a password: ")
    storeInfo = (userName, pwd)
    cursor.execute(add_data, storeInfo)
    conn.commit()
    
###If not need to make account used previous stored username and pwd
def prevAccnt():
    checkName = input("Please enter your username: ")
    checkPwd = input("Please enter your pwd: ")
    if checkPwd != pwd:
        print("Incorrect password.\n")
        main()
    elif pwd == "":
        print("No password saved, please make an account")
    

main()