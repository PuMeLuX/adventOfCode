def convertNumber(string) -> str:
    result = ""
    if string.isdigit():
        return string
    else:
        if string.find("one") != -1:
            return "1"
        elif string.find("two") != -1:
            return "2"
        elif string.find("three") != -1:
            return "3"
        elif string.find("four") != -1:
            return "4"
        elif string.find("five") != -1:
            return "5"
        elif string.find("six") != -1:
            return "6"
        elif string.find("seven") != -1:
            return "7"
        elif string.find("eight") != -1:
            return "8"
        elif string.find("nine") != -1:
            return "9"
        elif string.find("1") != -1:
            return "1"
        elif string.find("2") != -1:
            return "2"
        elif string.find("3") != -1:
            return "3"
        elif string.find("4") != -1:
            return "4"
        elif string.find("5") != -1:
            return "5"
        elif string.find("6") != -1:
            return "6"
        elif string.find("7") != -1:
            return "7"
        elif string.find("8") != -1:
            return "8"
        elif string.find("9") != -1:
            return "9"
    return result
    
def convertString(string) -> str:
    #print(string)
    result = ""
    letters = [*string]
    letterBuffer = ""
    for letter in letters:
        letterBuffer = letterBuffer + letter
        if convertNumber(letterBuffer).isdigit():
            result = result + convertNumber(letterBuffer)
            letterBuffer = letterBuffer[-1]
    return result 

########### Process input data ###########
file = open("./data", "r")
data = file.read()
data = data.split("\n")
#print(data)

result = 0;

for set in data:
    # turn into list of characters

    # Part 1
    #letters = [*set]

    # Part 2
    letters = [*convertString(set)]


    firstDigit = 0;
    lastDigit = 0;
    number = 0;

    # get first digit
    for i in range(0, len(letters)):
        if letters[i].isdigit():
            firstDigit = letters[i]
            break

    # get last digit
    for i in range(len(letters)-1, -1, -1):
        if letters[i].isdigit():
            lastDigit = letters[i]
            break
    
    # build number
    number = int(str(firstDigit) + str(lastDigit))
    #print(number)
    result = result + number

print("Result is: " + str(result))
