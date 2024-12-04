import mysql.connector

"""
The purpose of this file is to establish a connection to 
the MySQL database utilizing the following information:
    - Host          | 127.0.0.1
    - Username      | root
    - Password      | 12345
    - Database Name | calloway_scoring

The above information can be found within MySQL Workbench.
"""

# Connect to the database
# 'connection' is a MySQLConnection object
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='12345',
            database='calloway_scoring'
        )
        # Check if connection was successful
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None