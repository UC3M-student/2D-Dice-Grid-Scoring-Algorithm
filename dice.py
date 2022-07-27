from random import randint
import numpy as np

def points(n):
    score = 0
    try:
        for i in n:
            x = 0
            for y in i:
                if y%2 ==0:
                    x = x + 1
            if x ==4 or x==0:
             score +=20
    except:
        x = 0
        for i in n:
            if i%2 ==0:
                x = x + 1
        if x ==0 or x==4:
            score += 20
    
    return score   
            
dices = np.array([[randint(1,6),randint(1,6),randint(1,6),randint(1,6)],
                          [randint(1,6),randint(1,6),randint(1,6),randint(1,6)],
                          [randint(1,6),randint(1,6),randint(1,6),randint(1,6)],
                          [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]])
dices = np.reshape(dices,(4,4))

corners = [int(dices[0][0]),int(dices[0][len(dices)-1]),int(dices[len(dices)-1][0]),int(dices[len(dices)-1][len(dices)-1])]

rows = [row for row in dices]

column = [[row[0] for row in dices],[row[1] for row in dices],[row[2] for row in dices],[row[3] for row in dices]]

diagonals = [dices.diagonal(0),np.fliplr(dices).diagonal()]

total = np.sum(dices) + points(rows) + points(column) + points(diagonals)


print(dices, "Total points of this match is: ",total)
