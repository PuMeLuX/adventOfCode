## Part 1

file = open("./data", "r")
data = file.read()
data = data.split("\n\n")

top3 = [0, 0, 0]

max = 0

for set in data:
    setSplitted = set.split("\n")
    #print(setSplitted)

    localMax = 0

    for calories in setSplitted: 
        calories = int(calories)
        
        localMax = localMax + calories
    
    if localMax > max: 
        max = localMax

    ## Part 2

    if (top3[0] < localMax) & (top3[1] < localMax) & (top3[2] < localMax):
        top3[2] = top3[1]
        top3[1] = top3[0]
        top3[0] = localMax
    elif (top3[1] < localMax) & (top3[2] < localMax):
        top3[2] = top3[1]
        top3[1] = localMax
    elif (top3[2] < localMax):
        top3[2] = localMax

print("Elf with most Calories: " + str(max))

print("Top 3 Elfes: " + str(top3))

print("Sum of all Top 3 Elfes: " + str(top3[0] + top3[1] + top3[2]))

# for top in top3:
#     print(top)


