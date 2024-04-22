import unittest
import main
import mysql.connector

conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306, database = "bank_data")
cursor = conn.cursor()
user = cursor.execute("SELECT * FROM user_info2 WHERE userName = 'testUser'")

cursor.execute(f"SELECT balance FROM user_info2 WHERE userName = '{user[0]}'")
queryData = cursor.fetchone()
##print(f'Current balance: ${queryData[0]}')



class testMain(unittest.TestCase):
    def test_checkBal(self):
        result = main.checkBal(user)
        self.assertEqual(result, queryData[0])
