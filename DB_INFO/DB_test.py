from DB_Connect import connect_to_database
from DB_Interact import delete_row, insert_TeamName, fetch_TeamName


def main():
    #user_input = input("Please enter a team name: ")
    #print(user_input)
    connect_to_database()

main()