from flask import Flask, redirect, url_for, render_template
from flask_mysqldb import MySQL
from DB_Connect import connect_to_database
from DB_Interact import delete_Team, fetch_TeamNameInfo, insert_Scorecard, fetch_ScorecardID, insert_scores, fetch_scores
from create_Objects import create_ScorecardOBJs
from classes import Scorecard_OBJ

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/leaderboards")
def leaderboards():
    return render_template("leaderboards.html")

@app.route("/createScorecards")
def createScorecards():
    return render_template("createScorecards.html")

@app.route("/db_test")
def db_test():
    return str(fetch_TeamNameInfo('brettsTester'))

if __name__ == "__main__":
    app.run()