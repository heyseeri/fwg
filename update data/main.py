import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Db4',
                                         user='root',
                                         password='')

    sql_select_Query = "update Magazinetbl set MPRICE=1500 where MId = 1"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    print("data updated")
    cursor.close()
    connection.close()
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

