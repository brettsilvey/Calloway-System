import os
import numpy

scorecard = [4, 4, 9, 3, 8, 5, 7, 5, 5, 3, 5, 3, 5, 7, 4, 5, 5, 5]
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

# Print the Front, Back and Total Scores
print("Out: " + str(front9))
print("In: " + str(back9))
print("Total: " + str(front9+back9))

scorecard.sort(reverse=True)

for x in range(len(scorecard)):
    print(scorecard[x])