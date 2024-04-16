import mysql.connector
conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306, database = "bank_data")
cursor = conn.cursor()

add_data = "INSERT INTO user_info (userName, pwd) VALUES(%s, %s)"
accountFetch = "SELECT * FROM user_info WHERE userName = %s"
##conn.close()

###################################################################################

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
    
    try:
        cursor.execute(accountFetch, (checkName,))
    except Exception as e:
        if e.args[0] == "1042": 
            print("This user does not exist.")
        else:
            print("This user does not exist! Please try again!\n")
            tryAgain = input("Press the y key to continue: ")
            if tryAgain == "y": 
                checkName = ""
                main()
            else:
                quit()


    userInfo = cursor.fetchone()
    pwd = userInfo[1]
    print(pwd)
    checkPwd = input("Please enter your pwd: ")
    
    for i in range(3):
        if checkPwd != pwd:
            print(f'Incorrect password. You have used {i+1}/3 of your chances. \n')
            checkPwd = input("Please enter your pwd: ")
            
        elif pwd == "":
            print("No password saved, please make an account")
        elif checkPwd == pwd:
            print("Correct password entered. \n")
            print("How can we help you today?\n1. Make deposit\n2. Make withdraw\n")
            choice = input()

            if choice == "1":
                deposit(userInfo)
                ###Making deposit function right now

def deposit(user):
    depositAmt = int(input("How much would you like to deposit? \n"))
    


main()