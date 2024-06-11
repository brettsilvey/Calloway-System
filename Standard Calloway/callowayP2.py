import os
import math

# Method to return the amount of holes that are deducted bases on specified calloway dictionary
# Where the first element for each key value is the holes ddeucted and the second value is the handicap adjustment
def calc_Adjustment(grossScore):
    deductions = {
        73: (0.5, -2), 76:(1, -2), 81:(1.5, -2), 86:(2, -2), 91:(2.5, -2), 96:(3, -2), 101:(3.5, -2), 106:(4, -2), 111:(4.5, -2), 116:(5, -2), 121:(5.5, -2), 126:(6, -2),
        74: (0.5, -1), 77:(1, -1), 82:(1.5, -1), 87:(2, -1), 92:(2.5, -1), 97:(3, -1), 102:(3.5, -1), 107:(4, -1), 112:(4.5, -1), 117:(5, -1), 122:(5.5, -1), 127:(6, -1),
        70: (0.5, 0), 75:(0.5, 0), 78:(1, 0), 83:(1.5, 0), 88:(2, 0), 93:(2.5, 0), 98:(3, 0), 103:(3.5, 0), 108:(4, 0), 113:(4.5, 0), 118:(5, 0), 123:(5.5, 0), 128:(6, 0),
        71:(0, 1), 79:(1, 1), 84:(1.5, 1), 89:(2, 1), 94:(2.5, 1), 99:(3, 1), 104:(3.5, 1), 109:(4, 1), 114:(4.5, 1), 119:(5, 1), 124:(5.5, 1), 129:(6, 1),
        72:(0, 2), 80:(1, 2), 85:(1.5, 2), 90:(2, 2), 95:(2.5, 2), 100:(3, 2), 105:(3.5, 2), 110:(4, 2), 115:(4.5, 2), 120:(5, 2), 125:(5.5, 2), 130:(6, 2)
    }

    holes = deductions.get(grossScore)[0]
    adjustment = deductions.get(grossScore)[1]
    return holes, adjustment


# Take in scores from user
def score():
    scorecard = []
    hole = 1
    totalScore = 0
    while len(scorecard) != 18:
        curr = int(input("Enter Score for hole " + str(hole) + ": "))
        scorecard.append(curr)
        hole += 1
        totalScore += (curr)
    return scorecard, totalScore

# determine final score
def callyScore(scorecard, holeAmount, adjustment): # add hole amount, adjustment
    scorecard.pop(17) & scorecard.pop(16) # remove holes 17 & 18
    scorecard.sort(reverse = True) # sort the scorecard Highest -> lowest
    return scorecard




def main():
    # print(score()) - tests
    # print(calc_Adjustment(108)) - tests, where 108 is double bogey all the way
    # print(calc_Adjustment(score()[1]))

    print(callyScore(score()[0]))

main()
