from DB_Connect import connect_to_database
from DB_Interact import fetch_ScorecardID, fetch_scores, fetch_TeamNameInfo, fetch_TeamID
from classes import Scorecard_OBJ
import mysql.connector

"""
1. Find all teams with (best ball scorecards || scramble scorecards)
2. Find matching scorecard for each team
3. Find all scores for each scorecard
4. Create a list of Scorecard_OBJs
5. fill each Scorecard_OBJ with the appropriate information
6. return the list of Scorecard_OBJs
"""

# create a list of Scorecard_OBJs determined by Round Type
def create_ScorecardOBJs(roundType):
    # find all teams with the specified roundType
    connection = connect_to_database() # connect to the database
    try:
        if connection: # check if connection is successful
            cursor = connection.cursor() # create cursor object
            cursor.execute("SELECT * FROM scorecards WHERE roundType = %s", (roundType,)) #query the tuple matching teamName
            scorecards = cursor.fetchall() # fetch the tuple and set to teamID
    except mysql.connector.Error as err: # check for errors
        print(f"Error: {err}")
    finally:
        cursor.close() # delete the cursor
        connection.close() # close the connection

    # create a list of Scorecard_OBJs
    scorecardList = []
    scores = []
    for scorecard in scorecards:
        teamID = scorecard[1]
        teamName = fetch_TeamID(teamID)[1]
        scorecardID = scorecard[0]
        DB_scores = fetch_scores(scorecardID)
        for score in DB_scores:
            hole, strokes = score
            scores.append(score[1])
        scorecardList.append(Scorecard_OBJ(teamName, scores))
        scores = []
    return scorecardList