import mysql.connector

# Connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1', 
            user='root',
            password='12345',
            database='calloway_scoring'
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Print the data from the table
def fetch_data_from_table(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

# insert a new row into the table via user input
def insert_new_data(connection, table_name):
    try:
        cursor = connection.cursor()
        team_name = input("Enter the team name: ")
        team_score = input("Enter the team score: ")
        cursor.execute(f"INSERT INTO {table_name} (team_name, team_score) VALUES ('{team_name}', {team_score})")
        connection.commit()
        print("New row inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

# Main function
def main():
    connection = connect_to_database()
    if connection:
        fetch_data_from_table(connection, 'team_info')
        connection.close()

if __name__ == "__main__":
    main()