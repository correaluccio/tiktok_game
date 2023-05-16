from gameNumbers import generateNumber, countOcurrences, countMatches, feasible_number
    
    

class Board:
    def __init__(self):
        self.gameNumber = generateNumber()
        self.head = "|    Your guess      |   correct numbers   |   correct positions   |"
        self.rows = []
        self.win = False
        self.lose =False
        self.playerNumber = None;
        self.LastRow = []
    
    def addRow(self,playerNumber):
        if len(playerNumber) == 4 and feasible_number(playerNumber):
            self.playerNumber = playerNumber
            row = [str(self.playerNumber),str(countOcurrences(self.playerNumber, self.gameNumber)),str(countMatches(self.playerNumber, self.gameNumber))]
            self.rows.append(row)
            self.lastRow = row;
            self.printRows()
            self.finishGame()
        else:
            pass
    def printRows(self):
        row = self.lastRow
        print(f"|       {row[0]}         |          {row[1]}          |           {row[2]}           |")
    
    def finishGame(self):
        if self.gameNumber == self.playerNumber:
            self.win = True
            print(f"Congratulations you win in {len(self.rows)} attemps!")
        elif len(self.rows)>=100:
            print("Game Over!")
            self.lose=True
        else:
            pass


