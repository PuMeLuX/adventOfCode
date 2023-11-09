# function to calculate points for each pair, needed for Part 1 and 2
def calculatePoints(enemy, self) -> int:

    # A: Rock; B: Paper; C: Scissors
    # X: Rock; Y: Paper; Z: Scissors

    rockPoints = 1
    paperPoints = 2
    scissorsPoints = 3

    winPoints= 6
    drawPoints = 3
    losePoints = 0

    if enemy == 'A':
        if self == 'X': 
            return drawPoints + rockPoints
        elif self == 'Y':
            return winPoints + paperPoints
        elif self =='Z':
            return losePoints + scissorsPoints
        
    if enemy == 'B':
        if self == 'X': 
            return losePoints + rockPoints
        elif self == 'Y':
            return drawPoints + paperPoints
        elif self =='Z':
            return winPoints + scissorsPoints
    
    if enemy == 'C':
        if self == 'X': 
            return winPoints + rockPoints
        elif self == 'Y':
            return losePoints + paperPoints
        elif self =='Z':
            return drawPoints + scissorsPoints
        

## Calculate what i need to choose for Part 2
def calculateNeededChoice(enemy, outcome) -> str: 

    # A: Rock; B: Paper; C: Scissors
    # X: lose; Y: draw; Z: win
    # RETURN: X: Rock; Y: Paper; Z: Scissors

    if enemy == 'A': # Rock
        if outcome == 'X': # lose
            return 'Z'
        if outcome == 'Y': # draw
            return 'X'
        if outcome == 'Z': # win
            return 'Y'
        
    if enemy == 'B': # Paper
        if outcome == 'X': # lose
            return 'X'
        if outcome == 'Y': # draw
            return 'Y'
        if outcome == 'Z': # win
            return 'Z'
        
    if enemy == 'C': # Scissors
        if outcome == 'X': # lose
            return 'Y'
        if outcome == 'Y': # draw
            return 'Z'
        if outcome == 'Z': # win
            return 'X'


########### Process input data ###########
file = open("./data", "r")
data = file.read()
data = data.split("\n")
#print(data)


############### Part 1 ##################
score = 0

for pair in data:
    pair = pair.split(' ')
    
    # print(str(pair) + ' Points: ' + str(calculatePoints(pair[0], pair[1])))

    score += calculatePoints(pair[0], pair[1])

print('Part one: ' + str(score))


################# Part 2 #################

score = 0

for pair in data:
    pair = pair.split(' ')

    # print(str(pair) + ' Points: ' + str(calculatePoints(pair[0], pair[1])))

    pair[1] = calculateNeededChoice(pair[0], pair[1])
    score += calculatePoints(pair[0], pair[1])

print('Part two: ' + str(score))
