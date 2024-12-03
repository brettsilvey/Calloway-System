from DB_Connect import connect_to_database
from DB_Interact import delete_row, insert_TeamName, fetch_TeamName


def main():
    #user_input = input("Please enter a team name: ")
    #print(user_input)
    connection = connect_to_database()
    if connection:
        # do database stuff
        print("Connected to the database")
    connection.close()

main()