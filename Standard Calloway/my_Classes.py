import os
import math

map = {
     73: (0.5, -2), 76:(1, -2), 81:(1.5, -2), 86:(2, -2), 91:(2.5, -2), 96:(3, -2), 101:(3.5, -2), 106:(4, -2), 111:(4.5, -2), 116:(5, -2), 121:(5.5, -2), 126:(6, -2),
     74: (0.5, -1), 77:(1, -1), 82:(1.5, -1), 87:(2, -1), 92:(2.5, -1), 97:(3, -1), 102:(3.5, -1), 107:(4, -1), 112:(4.5, -1), 117:(5, -1), 122:(5.5, -1), 127:(6, -1),
     70: (0.5, 0), 75:(0.5, 0), 78:(1, 0), 83:(1.5, 0), 88:(2, 0), 93:(2.5, 0), 98:(3, 0), 103:(3.5, 0), 108:(4, 0), 113:(4.5, 0), 118:(5, 0), 123:(5.5, 0), 128:(6, 0),
     71:(0, 1), 79:(1, 1), 84:(1.5, 1), 89:(2, 1), 94:(2.5, 1), 99:(3, 1), 104:(3.5, 1), 109:(4, 1), 114:(4.5, 1), 119:(5, 1), 124:(5.5, 1), 129:(6, 1),
     72:(0, 2), 80:(1, 2), 85:(1.5, 2), 90:(2, 2), 95:(2.5, 2), 100:(3, 2), 105:(3.5, 2), 110:(4, 2), 115:(4.5, 2), 120:(5, 2), 125:(5.5, 2), 130:(6, 2)
}

class Leaderboard:
    def __init__(self, list, name):
        self.list = []
        self.name = name

    def getLeaderboard(self):
        for i in range(len(self.list)):
            print(self.list[i])

    def addScorecard(self, teamName, SC):
        self.list.append((teamName, SC))
        return self.list
    

class Scorecard:
    def __init__(self, list, name):
        self.list = list
        # self.list = []
        self.name = name
    
    # Return Name
    def getName(self):
        return self.name
    
    # Return Scorecard to User
    def getScorecard(self):
        return self.list
    
    def addScores(self, score):
        self.list.append(score)
        return

    # Sort List High -> Low
    def sort(self):
        temp = list(self.list)
        temp.pop(17)
        temp.pop(16)
        temp.sort(reverse = True)
        return temp
    
    # calculate & Return total Score
    def totalScore(self):
        totalScore = 0
        curr = 0
        while curr < 18:
            totalScore += self.list[curr]
            curr += 1
        return totalScore
    
    # Return holes deducted
    def getHoles(self):
        return map.get(self.totalScore())[0]
    
    # Return Handicap Adjustment
    def getAdjustment(self):
        return map.get(self.totalScore())[1]
    
    def getDeduction(self):
        # create temp variables so we do not destroy the real ones
        scorecard = list(self.sort()) # gives us access to the list, and it is sorted and last two are removed
        tempHoles = int(self.getHoles())
        tempAdjustment = int(self.getAdjustment())


        curr = 0
        total = 0
        while True:
            # check for 0.5
            if tempHoles == 0.5:
                total += math.ceil(scorecard[curr]/2)
                return total + tempAdjustment
             # check for 0
            elif tempHoles == 0:
                return total + tempAdjustment
            # if neither are true, update values
            total += scorecard[curr]
            curr +=1
            tempHoles -= 1
    
    # Return Calloway Score
    def cally(self):
        return int(self.totalScore()) - int(self.getDeduction())