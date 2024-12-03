import mysql.connector
from DB_Connect import connect_to_database

"""
-----------------------------------------------------------------------------------------
The purpose of this file is to fetch information from the team_info table from
 the calloway_scoring database. The following functions are available:
    - fetch_teamInfo()  | Fetch the team information from the table
    - insert_teamInfo() | Insert a new row into the table
-----------------------------------------------------------------------------------------
"""


# Delete a row from the team_info table
def delete_Team(teamName):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        # queryteamID = f"Select from teams where teamName = '{teamName}'"
        # cursor.execute(queryteamID)
        # teamID = cursor.fetchone()
        cursor.execute(f"DELETE FROM teams WHERE teamName = '{teamName}'")
        connection.commit()
        print("Row deleted successfully")
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor

# Insert a new teamName into the teams table
def insert_TeamName(teamName):
    connection = connect_to_database() # connect to the database
    try:
        cursor = connection.cursor() # create cursor object (Access R/W to DB)
        query = f"INSERT INTO teams (teamName) VALUES ('{teamName}')" # SQL query to insert a new teamName Row
        cursor.execute(query) # execute the SQL query
        connection.commit() # commit the changes to the database
        print(teamName + " created successfully") # print success message
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # close the curosor


def fetch_TeamNameInfo(teamName):

    """Function returns the tuple of a data set given a 
    team name ONLY If the team exists in the database
    - teamName: The name of the team to be queried
    - return: The tuple of the team information

    This function can be printed as a tuple, or as individual elements:
        ex. print(fetch_TeamNameInfo("tester")) -> (1, 'tester')
        ex. print(fetch_TeamNameInfo("tester")[0]) -> 1
        ex. print(fetch_TeamNameInfo("tester")[1]) -> tester

    This function has been modified so that SQL injection is not possible
    """

    connection = connect_to_database() # connect to database
    try:
        if connection: # check if connection is successful
            cursor = connection.cursor() # create cursor object
            cursor.execute("SELECT * FROM teams WHERE teamName = %s", (teamName,)) #query the tuple matching teamName
            teamID = cursor.fetchone() # fetch the tuple and set to teamID
            return teamID # return the information 
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor
        connection.close() # close the connection

# Insert new scorecard entry into the scorecards table
def insert_Scorecard(teamName, courseName, roundType):
    connection = connect_to_database() #connect to the database
    try:
        cursor = connection.cursor() # create cursor object
        queryTeamID = f"SELECT teamID from teams where teamName = '{teamName}'"
        cursor.execute(queryTeamID) # query TeamID using TeamName
        teamID = cursor.fetchone()
        if teamID: # if teamID exists
            queryInsert = f"Insert INTO scorecards (teamID, courseName, roundType) VALUES ('{teamID[0]}', '{courseName}', '{roundType}')" # insert teamID and CourseName into scorecard
            cursor.execute(queryInsert) # execute the query
            connection.commit() # commit the query to the database
            print("Scorecard created successfully") # print successful message
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close() # close the cursor


def fetch_ScorecardID(teamID, roundType):
    
    """ Fetches scorecardID based on teamName and roundType
    will need to include additional logic to handle a maximum 
    amount of scorecards per team.

    this function should be called utilized the information fetched from fetch_TeamNameInfo
    ex. teamID = fetch_TeamNameInfo("tester")
    ex. fetch_ScorecardID(teamID[0], "best ball")

    This function will return the tuple of the scorecard information, all four elements are accessible.

    This function has been modified so that SQL injection is not possible
"""

    connection = connect_to_database() # connect to the database
    try:
        if connection: # check if connection is successful
            cursor = connection.cursor()
            if teamID: # verify teamID exists
                cursor.execute("SELECT * FROM scorecards WHERE teamID = %s AND roundType = %s", (teamID, roundType))
                scorecard = cursor.fetchone() # print all scorecards relating to the teamID
                return scorecard
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor
        connection.close() # close the connection


# Insert a new a new set of scores into scorecard
def insert_scores(scorecardID, holeNum, strokes):
    connection = connect_to_database() # establish connection
    try:
        cursor = connection.cursor() # setup the cursor object
        query = f"INSERT INTO scores (scorecardID, holeNum, strokes) VALUES ('{scorecardID}', '{holeNum}', '{strokes}')"
        cursor.execute(query)
        connection.commit()
        print("Score added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()