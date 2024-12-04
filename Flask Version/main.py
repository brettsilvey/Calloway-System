from flask import Flask, redirect, url_for, render_template
from flask_mysqldb import MySQL
from DB_Connect import connect_to_database
from DB_Interact import delete_Team, insert_TeamName, fetch_TeamNameInfo, insert_Scorecard, fetch_ScorecardID, insert_scores, fetch_scores
from create_Objects import create_ScorecardOBJs
from classes import Scorecard_OBJ

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'calloway_scoring'

mysql = MySQL(app)

@app.route("/")
@app.route("/home")
def home():
    return "Hello"

@app.route("/leaderboards")
def leaderboards():
    return "This is the leaderboards page."

@app.route("/Scorecard")
def createScorecards():
    return "Create new Scorecards here"

@app.route("/db_test")
def db_test():
    return str(fetch_TeamNameInfo('tester'))

if __name__ == "__main__":
    app.run()