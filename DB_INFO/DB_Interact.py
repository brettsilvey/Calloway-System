import mysql.connector
from DB_Connect import connect_to_database

"""
The purpose of this file is to fetch information from the team_info table from the 
calloway_scoring database. The following functions are available:
    - fetch_teamInfo() | Fetch the team information from the table
    - insert_teamInfo() | Insert a new row into the table
"""


# Delete a row from the team_info table
def delete_row(teamName):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM team_info WHERE team_name = '{teamName}'")
            connection.commit()
            print("Row deleted successfully")
        except mysql.connector.Error as err: # check for errors
            print(f"Error: {err}")
        finally:
            cursor.close() # delete the cursor
            connection.close() # close the connection

# Insert a new row into the table given a team name from the user
def insert_TeamName(teamName):
    connection = connect_to_database() # connect to the database
    if connection: # verify connection
        try:
            cursor = connection.cursor() # create cursor object (Access R/W to DB)
            query = f"INSERT INTO team_info (team_name) VALUES ('{teamName}')" # SQL query to insert a new teamName Row
            cursor.execute(query) # execute the SQL query
            connection.commit() # commit the changes to the database
            print(teamName + " created successfully") # print success message
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close() # close the curosor
            connection.close() # close the connection

# Fetch the team information from the table
def fetch_TeamName(teamName):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM team_info WHERE team_name = '{teamName}'"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor
        connection.close() # close the connection