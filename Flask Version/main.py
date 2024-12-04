from flask import Flask, redirect, url_for, render_template, request, session
from flask_mysqldb import MySQL
from DB_Connect import connect_to_database
from DB_Interact import delete_Team, insert_TeamName, fetch_TeamNameInfo, insert_Scorecard, fetch_ScorecardID, insert_scores, fetch_scores
from create_Objects import create_ScorecardOBJs
from classes import Scorecard_OBJ, calloway_map

app = Flask(__name__)
app.secret_key ='secret_key'





@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

@app.route("/leaderboards")
def leaderboards():

    bestBallList = create_ScorecardOBJs("Best Ball")
    scrambleList = create_ScorecardOBJs("Scramble")
    strokePlayList = create_ScorecardOBJs("Standard")
    
    # Sort the lists by total score
    bestBallList = sorted(bestBallList, key=lambda x: x.totalScore())
    scrambleList = sorted(scrambleList, key=lambda x: x.totalScore())
    strokePlayList = sorted(strokePlayList, key=lambda x: x.totalScore())

    for scorecard in scrambleList:
        print(scorecard.getName())
        print(scorecard.totalScore())
        print(scorecard.getHoles())
        print(scorecard.cally())
        print("scramble list sorted")

    print("best ball list sorted")

    return render_template("leaderboards.html", bestBallList=bestBallList, scrambleList=scrambleList, strokePlayList=strokePlayList)

@app.route("/createScorecards")
def createScorecards():
    return render_template("createScorecards.html")

@app.route("/submit_scorecard_info", methods=["POST"])
def submit_scorecard_info():
    teamName = request.form["teamName"]
    courseName = request.form["courseName"]
    roundType = request.form["roundType"]

    insert_TeamName(teamName)
    teamID = fetch_TeamNameInfo(teamName)
    insert_Scorecard(teamID[0], courseName, roundType)
    scorecard = fetch_ScorecardID(teamID[0], roundType)

    # Store scorecard ID and current hole in session
    session['scorecard_id'] = scorecard[0]
    session['current_hole'] = 1

    return redirect(url_for("submit_scores"))


@app.route("/submit_scores", methods=["GET", "POST"])
def submit_scores():
    if request.method == "POST":
        scorecard_id = session.get('scorecard_id')
        current_hole = session.get('current_hole', 1)
        if not scorecard_id:
            return redirect(url_for("home"))

        # Insert score for the current hole
        strokes = request.form["strokes"]
        insert_scores(scorecard_id, current_hole, strokes)

        # Update the current hole
        current_hole += 1
        if current_hole > 18:
            return redirect(url_for("home"))
        session['current_hole'] = current_hole

    current_hole = session.get('current_hole', 1)
    return render_template("submit_scores.html", hole=current_hole)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)