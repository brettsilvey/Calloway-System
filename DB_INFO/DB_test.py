from DB_Connect import connect_to_database
from DB_Interact import delete_Team, insert_TeamName, fetch_TeamNameInfo, insert_Scorecard, fetch_ScorecardID, insert_scores, fetch_scores


def main():
    #user_input = input("Please enter a team name: ")
    #print(user_input)
    print("Hello World - Welcome to the Calloway Scoring system")
    create_entireEntry()
    
    # teamID = fetch_TeamNameInfo('tester')
    
    # prints out team information
    # if teamID:
    #     print("Team exists")
    #     print("Tuple: " + str(teamID))
    #     print("Team ID: " + str(teamID[0]))
    #     print("Team Name: " + str(teamID[1]))
    # else:
    #     print("Team does not exist")

    # prints out scorecard information

    # scorecard = fetch_ScorecardID(teamID[0], "best ball")

    # if scorecard:
    #     print("Scorecard exists")
    #     print("Tuple: " + str(scorecard))
    #     print("Scorecard ID: " + str(scorecard[0]))
    #     print("Team ID: " + str(scorecard[1]))
    #     print("Course Name: " + str(scorecard[2]))
    #     print("Round Type: " + str(scorecard[3]))

    # print(fetch_scores(scorecard[0]))
    
    # insert some scores
    # hole = 1
    # while hole < 19:
    #     strokes = input(f"Enter the number of strokes for hole {hole}: ")
    #     insert_scores(scorecard[0], hole, strokes)
    #     hole += 1

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

