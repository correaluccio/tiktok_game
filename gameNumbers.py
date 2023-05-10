import random

def countOcurrences(playerNumber,gameNumber):
    gameNumber = str(gameNumber)
    playerNumber = str(playerNumber)
    playerNumber_list = []
    for i in playerNumber:
        playerNumber_list.append(i)
    aux = 0
    for j in gameNumber:
       aux+= playerNumber_list.count(j)
    return aux

def countMatches(playerNumber,gameNumber):
    gameNumber = str(gameNumber)
    playerNumber = str(playerNumber)
    if len(playerNumber) == 4:
        aux = 0
        for i in range(4):
            if gameNumber[i] == playerNumber[i]:
                        aux+=1
        return aux
    else:
        return 0
def generateNumber():
    numbers = [1,2,3,4,5,6,7,8,9]
    digits = ""
    for i in range(4):
        numberchoice = random.choice(numbers)
        digits += str(numberchoice)
        numbers.remove(numberchoice)
    return digits
    
