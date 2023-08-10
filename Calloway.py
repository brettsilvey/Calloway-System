import os
import math

#-------------------------------------scorecards ------------------------------------------------
DressForLess = [4, 4, 5, 3, 4, 3, 5, 5, 5, 3, 4, 5, 4, 4, 5, 3, 6, 4] ### 76 - Logan and Preston
# Osama = [4, 4, 7, 3, 6, 3, 3, 5, 4, 4, 6, 4, 5, 6, 5, 3, 5, 5] ### 82 - Jordan and Jared



#------------------------------------------------------------------------------
# Make this into a method? 
#Ask for the scores for each hole and append to scorecard ---  THIS WORKS
# hole = 1
# while hole <= 18:
#     userInput = int(input("Enter Score for Hole " + str(hole) + ": "))
#     scorecard.append(userInput)
#     hole += 1
#-------------------------------------------------------------------------------

# Use this later for print front and back nine scores
    # front9 = 0
    # back9 = 0
    # for x in range(0,9):
    #     front9 += scorecard[x]
    # for x in range(9, 18):
    #     back9 += scorecard[x]

    # totalScore = front9 + back9

def scoring (scorecard):
    total = 0
    for x in range(len(scorecard)):
        total += scorecard[x]
    return total


def intSplit(func, x):
    list_of_digits = [int(i) for i in str(func(x))]
    # print("Last Digit of Score: " + str(list_of_digits[-1]))
    return list_of_digits[-1]


# use to determine if -2, -1, 0, +1, +2 --- This works great
def handicapAdjustment(func, x):
    if intSplit(func, x) == 6 or intSplit(func, x) == 1:
        adjustment = -2
        return adjustment
    elif intSplit(func, x) == 7 or intSplit(func, x) == 2:
        adjustment = -1
        return adjustment
    elif intSplit(func, x) == 8 or intSplit(func, x) == 3:
        adjustment = 0
        return adjustment
    elif intSplit(func, x) == 9 or intSplit(func, x) == 4:
        adjustment = 1
        return adjustment
    elif intSplit(func, x) == 0 or intSplit(func, x) == 5:
        adjustment = 2
        return adjustment
        

# Determine the Handicap deduction -- DO NOT TOUCH THIS ONE
# def initDeduction(totScore, scorecard):

    # No Deduction - 72 and lower
    if totScore <= 72:
        print("Calloway Score = " + str(totScore))
    
    # Half of worst hole - 73, 74, 75
    elif totScore > 72 and totScore <= 75:
        temp = totScore - 72
        deduction = math.ceil(scorecard[0] / 2)

    # Full Hole Deduction - 76, 77, 78, 79, 80
    elif totScore > 75 and totScore <= 80:
        deduction = math.ceil(scorecard[0] + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 1 1/2 Hole Deduction - 81, 82, 83, 84, 85
    elif totScore > 80 and totScore <= 85:          
        deduction = math.ceil((scorecard[0] + (scorecard[1] / 2)) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 2 Hole Deduction - 86, 87, 88, 89, 90
    elif totScore > 85 and totScore <= 90:
        deduction = scorecard[0] + scorecard[1]

    # 2 1/2 Hole Deduction - 91, 92, 93, 94, 95
    elif totScore > 90 and totScore <= 95:
        deduction = math.ceil((scorecard[0] + scorecard[1] + (scorecard[2] / 2)) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 3 Hole Deduction - 96, 97, 98, 99, 100
    elif totScore > 95 and totScore <= 100:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2]) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 3 1/2 Hole Deduction - 101, 102, 103, 104, 105
    elif totScore > 100 and totScore <= 105:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + (scorecard[3] / 2)) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 4 Hole Deduction - 106, 107, 108, 109, 110
    elif totScore > 105 and totScore <= 110:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3]) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 4 1/2 Hole Deduction - 111, 112, 113, 114, 115
    elif totScore > 110 and totScore <= 115:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + (scorecard[4] / 2)) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 5 Hole Deduction - 116, 117, 118, 119, 120
    elif totScore > 115 and totScore <= 120:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4]) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 5 1/2 Hole Deduction - 121, 122, 123, 124, 125
    elif totScore > 120 and totScore <= 125:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4] + (scorecard[5] / 2)) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    # 6 Hole Deduction - 126, 127, 128, 129, 130
    elif totScore > 125 and totScore <= 130:
        deduction = math.ceil((scorecard[0] + scorecard[1] + scorecard[2] + scorecard[3] + scorecard[4] + scorecard[5]) + handicapAdjustment(totScore))
        print("Total Deduction: " + str(deduction))

    else:
        print("Your score is too high - Golf might not be for you!")


# Determine the Handicap deduction
def initDeduction(func, x):

    # No Deduction - 72 and lower
    if func(x) <= 72:
        print("Calloway Score = " + str(func(x)))
    
    # Half of worst hole - 73, 74, 75
    elif func(x) > 72 and func(x) <= 75:
        deduction = math.ceil(x[0] / 2)
        return deduction

    # Full Hole Deduction - 76, 77, 78, 79, 80
    elif func(x) > 75 and func(x) <= 80:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0])
        return deduction

    # 1 1/2 Hole Deduction - 81, 82, 83, 84, 85
    elif func(x) > 80 and func(x) <= 85:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)     
        deduction = math.ceil(x[0] + (x[1] / 2))
        return deduction

    # 2 Hole Deduction - 86, 87, 88, 89, 90
    elif func(x) > 85 and func(x) <= 90:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = x[0] + x[1]
        return deduction

    # 2 1/2 Hole Deduction - 91, 92, 93, 94, 95
    elif func(x) > 90 and func(x) <= 95:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + (x[2] / 2))
        return deduction

    # 3 Hole Deduction - 96, 97, 98, 99, 100
    elif func(x) > 95 and func(x) <= 100:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2])
        return deduction

    # 3 1/2 Hole Deduction - 101, 102, 103, 104, 105
    elif func(x) > 100 and func(x) <= 105:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + (x[3] / 2))
        return deduction

    # 4 Hole Deduction - 106, 107, 108, 109, 110
    elif func(x) > 105 and func(x) <= 110:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + x[3])
        return deduction

    # 4 1/2 Hole Deduction - 111, 112, 113, 114, 115
    elif func(x) > 110 and func(x) <= 115:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + x[3] + (x[4] / 2))
        return deduction

    # 5 Hole Deduction - 116, 117, 118, 119, 120
    elif func(x) > 115 and func(x) <= 120:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + x[3] + x[4])
        return deduction

    # 5 1/2 Hole Deduction - 121, 122, 123, 124, 125
    elif func(x) > 120 and func(x) <= 125:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + x[3] + x[4] + (x[5] / 2))
        return deduction

    # 6 Hole Deduction - 126, 127, 128, 129, 130
    elif func(x) > 125 and func(x) <= 130:
        x.pop(16)
        x.pop(16)
        x.sort(reverse = True)
        deduction = math.ceil(x[0] + x[1] + x[2] + x[3] + x[4] + x[5])
        return deduction

    else:
        print("Your score is too high - Golf might not be for you!")


def main(scorecard):
    print("Total Score: " + str(scoring(scorecard)))
    print("Int Split: " + str(intSplit(scoring, scorecard)))

    handiCapdeduction = handicapAdjustment(scoring, scorecard)
    deduc = (initDeduction(scoring, scorecard))



    # print("Handicap Adjustment: " + str(handiCapdeduction))
    # print("Initial Deduction: " + str(initDeduction(scoring, scorecard)))




main(DressForLess)