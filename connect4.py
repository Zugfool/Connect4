import turtle as t
timmy=t.Turtle()
timmy.pensize(6);timmy.penup();timmy.speed("fastest");timmy.setposition(0,100);timmy.hideturtle()
screen=t.Screen()

def arena(x):
    rows=[]
    for j in range(0,x):
        row=""
        row+="|"
        for i in range(0,10):
            row+="&"
        row+="|"
        rows.append(row)
    return rows

Players=[]; game_won = False; round = 0;cond=False
for i in range(2):
    name=screen.textinput("","What is your name?")
    Players.append(name)

table=arena(7)
timmy.seth(270)
for i in table:
    timmy.write(i,align="center",font=("Aria",50,"normal"))
    timmy.forward(50)
    

def classic_round(x):
    if x%2==1:
        player=Players[0]
    else:
        player=Players[1]
    print(f"{player} moves")
    column=screen.textinput("","Select a column to put your piece: ")
    column=int(column)
    done=False
    row=0
    while done==False:
        row=row-1
        if row==-8:
            print("That column is already full. Try Again")
            return(x)
        elif table[row][column]=="&":
            change= list(table[row])
            change[column]=player[0]
            change="".join(change)
            table[row]=change
            done=True
            screen.clearscreen()
            timmy.setpos(0,60)
            for i in table:
                timmy.write(i,align="center",font=("Aria",50,"normal"))
                timmy.forward(50)
            return(table,player,column,row)
        
def yatay_kontrol(table,player,row):
    game_won=False; tekrar=1; past=""
    for i in table[row]:
        if i==past and i!="&":
            tekrar+=1
            if tekrar==4:
                screen.clearscreen()
                timmy.write(f"{player} has won in {-row}. row.",align="center",font=("Aria",50,"normal")); game_won=True
                return(game_won)
        else:
            tekrar=1;past=i

def dikey_kontrol(table,player,column):
    game_won=False; tekrar=1; past=""
    for i in table:
        if i[column]==past and i[column]!="&":
            tekrar+=1
            if tekrar==4:
                screen.clearscreen()
                timmy.write(f"{player} has won in {column}. column.",align="center",font=("Aria",50,"normal")); game_won=True
                return(game_won)
        else:
            tekrar=1;past=i[column]

def cross_right(table,player):
    game_won=False
    for i in range(1,5):
        for j in range(1,8):
            if table[-i][j]!="&":
                if table[-i][j] == player[-1] and table[-i-1][j+1] == player[-1] and table[-i-2][j+2] == player[-1] and table[-i-3][j+3] == player[-1]:
                    game_won=True; screen.clearscreen(); timmy.write(f"{player} has won. Congrats!",align="center",font=("Aria",50,"normal"))
                    return(game_won)

def cross_left(table,player):
    game_won=False
    for i in range(1,5):
        for j in range(4,11):
            if table[-i][j]!="&":
                if table[-i][j] == player[-1] and table[-i-1][j-1] == player[-1] and table[-i-2][j-2] == player[-1] and table[-i-3][j-3] == player[-1]:
                    game_won=True;screen.clearscreen(); timmy.write(f"{player} has won. Congrats!",align="center",font=("Aria",50,"normal"))
                    return(game_won)

while game_won == False:
    round+=1
    round_outcome=classic_round(round)
    if type(round_outcome)==int: #hamle yapamadıktan sonra tekrardan denetiyor
        round=round-1
    else:
        game_outcome1 = yatay_kontrol(round_outcome[0],round_outcome[1],round_outcome[3])
        game_outcome2 = dikey_kontrol(round_outcome[0],round_outcome[1],round_outcome[2])
        game_outcome3 = cross_right(round_outcome[0],round_outcome[1])
        game_outcome4 = cross_left(round_outcome[0],round_outcome[1])
        ending=[game_outcome1,game_outcome2,game_outcome3,game_outcome4]
        for i in ending:
            if i==True:
                game_won=True