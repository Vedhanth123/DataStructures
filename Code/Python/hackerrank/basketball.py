# python program to solve basket ball problem in hackerrank

# Maria plays college basketball and wants to go pro.
# Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points
# and least points in a game. Points scored in the first game establish her record for the season
# and she begins counting from there.

# For example:

#                                  Count
# Game  Score  Minimum  Maximum   Min Max
#  0      12     12       12       0   0
#  1      24     12       24       0   1
#  2      10     10       24       1   1
#  3      24     10       24       1   1

#  Given Maria's scores for a season, find and print the number of times
#  she breaks her records for most and least points scored during the season.

def breakingRecords(scores):
    # counting no of highest and no of lowest scores
    highest_count = lowest_count = 0
    # firstly we'll take first element of array and assign to both our highest and lowest scores
    highest = lowest = scores[0]
    # Then we'll compare next elements to highest and lowest
    for x in range(len(scores)):
        # if any one is highest of lowest we'll reassign lowest and highest values
        if(highest > scores[x]):
            # Along with that we'll note down how many assignments done to highest and lowest
            highest_count += 1
            highest = scores[x]
        elif(lowest < scores[x]):
            lowest_count += 1
            lowest = scores[x]
        else:
            continue

    # lastly we'll print that down

    return lowest_count, highest_count

print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
