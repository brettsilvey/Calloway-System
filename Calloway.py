import os
import math

scorecard = [3, 3, 3, 3, 5, 2, 7, 5, 4, 4, 4, 5, 5, 5, 3, 3, 4, 7]
# scorecard = []

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

def CallowayScoring(totScore, scorecard):
    if totScore <= 72:                              # No Deduction
        print("Calloway Score = " + str(totScore))
    elif totScore > 72 and totScore <= 75:          # Half of worst hole
        temp = totScore - 72
        deduction = scorecard[0] / 2
        print("Calloway Deduction: " + str(math.ceil(deduction)))

    
CallowayScoring(75, scorecard)