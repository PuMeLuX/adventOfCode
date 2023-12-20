# Define max values for cubes colors
max_blue = 14
max_red = 12
max_green = 13

def main():
    ########### Process input data ###########
    file = open("./data", "r")
    data = file.read()
    data = data.split("\n")
    #print(data)

    print("Solution Part 1: " + str(part1(data)))
    print("Solution Part 2: " + str(part2(data)))

def part1(data):
    result = 0
    for bag in data:
        id = getGameId(bag)
        gameInputs = getGameInputs(bag)
        blue = findMaxForColor(gameInputs, 'blue')
        green = findMaxForColor(gameInputs, 'green')
        red = findMaxForColor(gameInputs, 'red')

        if (blue <= max_blue) & (red <= max_red) & (green <= max_green):
            result = result + int(id)

    return result

def part2(data):
    result = 0
    for bag in data:
        bagPower = calculatePower(bag)
        result += bagPower

    return result

def getGameId(bag) -> int:  
    return(bag.split(":")[0].split(" ")[1])

def getGameInputs(bag):
    return(bag.split(":")[1].split(";"))

def findMaxForColor(bagInputs, color):
    #print(bagInputs)
    localMax = 0
    for pull in bagInputs:
        #print(pull)
        for colorPull in pull.split(","):
            colorPull = colorPull.strip()
            tupel = colorPull.split(" ")
            if tupel[1] == color:
                if int(tupel[0]) > localMax:
                    localMax = int(tupel[0])
                    #print(tupel)
    #print(color + " max " + str(localMax))
    return localMax

def calculatePower(bag):
    gameInputs = getGameInputs(bag)
    blue = findMaxForColor(gameInputs, 'blue')
    green = findMaxForColor(gameInputs, 'green')
    red = findMaxForColor(gameInputs, 'red')

    return blue * green * red


if __name__ == "__main__":
    main()