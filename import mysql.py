##import mysql.connector
##conn = mysql.connector.connect(host= '127.0.0.1', user = 'root', passwd="WaffleMan@978", port=3306, database = "testdb")
##cursor = conn.cursor()
##cursor.execute("CREATE DATABASE testdb")
##cursor.execute("CREATE TABLE test_table (name VARCHAR(255), age INTEGER(10))")

""" testQuery = "SELECT * FROM test_table"
cursor.execute(testQuery)
for item in cursor:
    print(item) """
##conn.close()

##cursor.execute("ALTER TABLE user_info ADD COLUMN balance INT")
##cursor.execute("UPDATE table_name SET name = %s WHERE id = 1", (name,))