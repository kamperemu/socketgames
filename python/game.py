game = [["-","-","-"],["-","-","-"],["-","-","-"]]


def displaygame():
    for i in game:
        for j in i:
            print(j,end=" ")
        print()

def decidegame(sym):
    status = ""
    for i in game:
        if i == [sym,sym,sym]:
            status="win"
    for i in range(len(game)):
        if [game[0][i],game[1][i],game[2][i]]==[sym,sym,sym]:
            status="win"
    if [game[0][0],game[1][1],game[2][2]] == [sym,sym,sym]:
        status="win"
    if [game[0][2],game[1][1],game[2][0]] == [sym,sym,sym]:
        status="win"
    if status != "win":
        status = "tie"
        for i in range(len(game)):
            for j in game[i]:
                if j == "-":
                    status = "continue"
    return status
    
    

def makemove(playersymbol):
    x = 0
    y = 0
    try:
        x = int(input("input x pos (1-3): "))
        y = int(input("input y pos (1-3): "))
    except ValueError:
        print("you can only input (1,2,3)")
        makemove(playersymbol)
    try:
        if game[y-1][x-1] == "-":
            game[y-1][x-1] = playersymbol
        else:
            print("invalid move")
            makemove(playersymbol)
    except IndexError:
        print("only numbers (1,2,3)")
        makemove(playersymbol)
    print(decidegame(playersymbol))



while True:
    displaygame()
    makemove("X")
    displaygame()
    makemove("O")