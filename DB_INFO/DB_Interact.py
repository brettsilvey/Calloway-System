import mysql.connector
from DB_Connect import connect_to_database

"""
The purpose of this file is to fetch information from the team_info table from the 
calloway_scoring database. The following functions are available:
    - fetch_teamInfo() | Fetch the team information from the table
    - insert_teamInfo() | Insert a new row into the table
"""


# Delete a row from the team_info table
def delete_Team(teamName):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        queryteamID = f"Select from teams where teamName = '{teamName}'"
        cursor.execute(queryteamID)
        teamID = cursor.fetchone()
        cursor.execute(f"DELETE FROM teams WHERE team_name = '{teamID}'")
        connection.commit()
        print("Row deleted successfully")
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor

# Insert a new row into the table given a team name from the user
def insert_TeamName(teamName):
    connection = connect_to_database() # connect to the database
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

# Fetch the team information from the table
def fetch_TeamName(teamName):
    try:
        connection = connect_to_database()
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

# Insert new scorecard
def insert_Scorecard(teamName, courseName):
    connection = connect_to_database() #connect to the database
    try:
        cursor = connection.cursor() # create cursor object
        queryTeamID = f"SELECT teamID from teams where teamName = '{teamName}'"
        cursor.execute(queryTeamID) # query TeamID using TeamName
        teamID = cursor.fetchone()
        if teamID: # if teamID exists
            queryInsert = f"Insert INTO scorecards('{teamID}', '{courseName}')" # insert teamID and CourseName into scorecard
            cursor.execute(queryInsert) # execute the query
            connection.commit() # commit the query to the database
            print("Scorecard created successfully") # print successful message
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close() # close the cursor

# Fetch Information from Scorecard
def fetch_Scorecard(teamName):
    try:
        connection = connect_to_database() # connect to the database - this can all be removed and placed in the maine function
        cursor = connection.cursor()
        queryTeamName = f"SELECT teamID from teams where teamName = '{teamName}'"
        cursor.execute(queryTeamName)
        teamID = cursor.fetchone()
        if teamID:
            insertQuery = f"SELECT * FROM scorecard WHERE teamID = '{teamID}'"
            cursor.execute(insertQuery)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor