import mysql.connector
conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306, database = "bank_data")
cursor = conn.cursor()

add_data = "INSERT INTO user_info2 (userName, pwd, balance) VALUES(%s, %s, %s)"
accountFetch = "SELECT * FROM user_info2 WHERE userName = %s"
deposit = "UPDATE user_info2 SET balance = balance + %s WHERE userName = %s"
cursor.execute("UPDATE user_info2 SET balance = balance + 100 WHERE userName = 'testUser'")
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
####################################################################################################
def newAccnt():
    userName = input("Please provide a username: ")
    pwd = input("Please provide a password: ")
    balance = input("Please provide a starting balance: ")
    storeInfo = (userName, pwd, balance)
    cursor.execute(add_data, storeInfo)
    conn.commit()
    print("Account successfully added, sign in to access bank information.")
    main()
    
###If not need to make account used previous stored username and pwd
####################################################################################################
def prevAccnt():
    checkName = input("Please enter your username: ")
    
    ##Checks if account exists
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
    
    ###checks if pwd is correct
    for i in range(3):
        if checkPwd != pwd:
            print(f'Incorrect password. You have used {i+1}/3 of your chances. \n')
            checkPwd = input("Please enter your pwd: ")
            
        elif pwd == "":
            print("No password saved, please make an account")
        elif checkPwd == pwd:
            print("Correct password entered. \n")
            ###choices
            print("How can we help you today?\n1. Make deposit\n2. Make withdraw\n3. Change Username \n4. Change Password\n5. Exit\n")
            choice = input()

            if choice == "1":
                deposit(userInfo)
                break
            if choice == "2":
                withdraw(userInfo)
                break
            if choice == "3":
                changeName(userInfo)
                break
            if choice == "4":
                changePwd(userInfo)
            if choice == "5":
                print("Thank you for using our bank, have a wonderful day!")
                quit()
    print("Maximum attempts reached, please try again.")
    main()



###Deposit function
####################################################################################################

def deposit(user):
    print(f'Current balance = ${user[2]}')
    depositAmt = int(input("How much would you like to deposit? \n"))
    cursor.execute(f'UPDATE user_info2 SET balance = balance + {depositAmt} WHERE userName = "{user[0]}"')
    conn.commit()
    print("Deposit success!\n")
    choice(user)

###Withdraw function
####################################################################################################

def withdraw(user):
    print(f'Current balance = ${user[2]}')
    withdrawAmt = int(input("How much would you like to withdraw? \n"))
    if user[2] < withdrawAmt:
        print("Insufficient funds in your account, please try again")
        withdraw(user)
    else:
        cursor.execute(f'UPDATE user_info2 SET balance = balance - {withdrawAmt} WHERE userName = "{user[0]}"')
        conn.commit()
        print("Withdraw success!")
    choice(user)
    
###change username function
####################################################################################################

def changeName(user):
    nameChange = input("What would you like to change your username to? \n")
    confirm = input(f'"{nameChange}" is what you entered, does this seem correct (y/n)? \n')

    if confirm == "y":
        print("Changing name...")
        cursor.execute(f'UPDATE user_info2 SET userName = "{nameChange}" WHERE userName = "{user[0]}"')
        conn.commit()
        print("Name successfully changed! \n")

        choice(user)


    if confirm == "n":
        again = input("Would you like to try again (y/n)?")
        if again == "y":
            changeName(user)
        if again == "n":
            choice(user)

###Change password function
####################################################################################################

def changePwd(user):
    pwdChange = input("What would you like to change your password to? \n")
    confirm = input(f'"{pwdChange}" is what you entered, does this seem correct (y/n)? \n')

    if confirm == "y":
        print("Changing name...")
        cursor.execute(f'UPDATE user_info2 SET pwd = "{pwdChange}" WHERE userName = "{user[0]}"')
        conn.commit()
        print("Password successfully changed! \n")

        choice(user)


    if confirm == "n":
        again = input("Would you like to try again (y/n)?")
        if again == "y":
            changePwd(user)
        if again == "n":
            choice(user) 

###gives user options for where to go next, made to condense code
####################################################################################################

def choice(user):
    print("\n Is there anything else we can help with today?")
    print("\n1. Make deposit\n2. Make withdraw\n3. Change Username \n4. Change Password\n5. Exit\n")
    nextChoice = input()
    if nextChoice == "1":
        deposit(user)
    if nextChoice == "2":
        withdraw(user)
    if nextChoice == "3":
        changeName(user)
    if nextChoice == "4":
        changePwd(user)
    if nextChoice == "5":
        print("Thank you for using our bank, have a wonderful day!")
        quit()    



main()