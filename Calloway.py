import os
import math

# scorecard = [3, 3, 3, 3, 5, 2, 7, 5, 4, 4, 4, 5, 5, 5, 3, 3, 4, 7]  ###total = 75
# scorecard = [4, 4, 5, 3, 4, 3, 5, 5, 5, 3, 4, 5, 4, 4, 5, 3, 6, 4]
scorecard  = [4, 5, 9, 4, 5, 4, 5, 5, 5, 3, 5, 4, 6, 5, 6, 4, 5, 5]

#Ask for the scores for each hole and append to scorecard ---  THIS WORKS
# hole = 1
# while hole <= 18:
#     userInput = int(input("Enter Score for Hole " + str(hole) + ": "))
#     scorecard.append(userInput)
#     hole += 1

front9 = 0
back9 = 0

# Find the Total for front 9 holes
for x in range(0, 9):
    front9 += scorecard[x]
# Find the Total for back 9 holes
for x in range(9, 18):
    back9 += scorecard[x]

totalScore = front9+back9

# Print the Front, Back and Total Scores
print("Out: " + str(front9))
print("In: " + str(back9))
print("Total: " + str(totalScore))

scorecard.pop(16)
scorecard.pop(16)


scorecard.sort(reverse=True)

count = 0
for x in range(len(scorecard)):
    count += 1
    print(scorecard[x])

print(count)


# split the total score into seperate digits - the last digit will be used to determine the handicap adjustment
def intSplit(totalScore):
    list_of_digits = [int(i) for i in str(totalScore)]
    return list_of_digits[-1]

# use to determine if -2, -1, 0, +1, +2
def handicapAdjustment(totalScore):
    if intSplit(totalScore) =

# Determine the Handicap deduction
def initDeduction(totScore, scorecard):

    # No Deduction - 72 and lower
    if totScore <= 72:
        print("Calloway Score = " + str(totScore))
    
    # Half of worst hole - 73, 74, 75
    elif totScore > 72 and totScore <= 75:
        temp = totScore - 72
        deduction = math.ceil(scorecard[0] / 2)

    # Full Hole Deduction - 76, 77, 78, 79, 80
    elif totScore > 75 and totScore <= 80:
        deduction = scorecard[0]

    # 1 1/2 Hole Deduction - 81, 82, 83, 84, 85
    elif totScore > 80 and totScore <= 85:          
        deduction = math.ceil(scorecard[0] + (scorecard[1] / 2))

    # 2 Hole Deduction - 86, 87, 88, 89, 90
    elif totScore > 85 and totScore <= 90:
        deduction = scorecard[0] + scorecard[1]

    # 2 1/2 Hole Deduction - 91, 92, 93, 94, 95
    elif totScore > 90 and totScore <= 95:
        deduction = math.ceil(scorecard[0] + scorecard[1] + (scorecard[2] / 2))

    # 3 Hole Deduction - 96, 97, 98, 99, 100
    elif totScore > 95 and totScore <= 100:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2])

    # 3 1/2 Hole Deduction - 101, 102, 103, 104, 105
    elif totScore > 100 and totScore <= 105:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + (scorecard[3] / 2))

    # 4 Hole Deduction - 106, 107, 108, 109, 110
    elif totScore > 105 and totScore <= 110:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3])

    # 4 1/2 Hole Deduction - 111, 112, 113, 114, 115
    elif totScore > 110 and totScore <= 115:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + (scorecard[4] / 2))

    # 5 Hole Deduction - 116, 117, 118, 119, 120
    elif totScore > 115 and totScore <= 120:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4])

    # 5 1/2 Hole Deduction - 121, 122, 123, 124, 125
    elif totScore > 120 and totScore <= 125:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4] + (scorecard[5] / 2))

    # 6 Hole Deduction - 126, 127, 128, 129, 130
    elif totScore > 125 and totScore <= 130:
        deduction = math.ceil(scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4] + scorecard[5])

    else:
        print("Your score is too high - Golf might not be for you!")











    
initDeduction(93, scorecard)
# intSplit(totalScore)