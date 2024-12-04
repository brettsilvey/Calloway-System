from DB_Connect import connect_to_database
from DB_Interact import delete_Team, insert_TeamName, fetch_TeamNameInfo, insert_Scorecard, fetch_ScorecardID, insert_scores, fetch_scores
from create_Objects import create_ScorecardOBJs
from classes import Scorecard_OBJ

def main():
    #user_input = input("Please enter a team name: ")
    #print(user_input)
    print("Hello World - Welcome to the Calloway Scoring system")
    # create_entireEntry()

    scorecardList = create_ScorecardOBJs("Scramble")

    print(len(scorecardList))

    print("Before Sorting")
    # print values before sorting
    for scorecard in scorecardList:
        print(scorecard.getName())
        # print(scorecard.getScorelist())
        print(scorecard.totalScore())
        # print(scorecard.getHoles())
        print(scorecard.cally())


    # sortedScorecard = sorted(scorecardList, key=lambda x: x.totalScore())
    # print("After Sorting")
    # #print values after sorting
    # for scorecard in sortedScorecard:
    #     print(scorecard.getName())
    #     print(scorecard.getScorelist())
    #     print(scorecard.totalScore())

def create_entireEntry():
    teamName = input("Enter the team name: ")
    courseName = input("Enter the course name: ")
    roundType = input("Enter the round type: ")

    insert_TeamName(teamName)
    teamID = fetch_TeamNameInfo(teamName)
    insert_Scorecard(teamID[0], courseName, roundType)
    scorecard = fetch_ScorecardID(teamID[0], roundType)

    # insert some scores
    hole = 1
    while hole < 19:
        strokes = input(f"Enter the number of strokes for hole {hole}: ")
        insert_scores(scorecard[0], hole, strokes)
        hole += 1

main()

