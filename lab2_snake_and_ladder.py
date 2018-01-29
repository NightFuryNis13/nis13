import random # Imports the random library

ctr=0
print("WELCOME!!LET'S BEGIN THE GAME OF SNAKE AND LADDER")
print("YOUR CURRENT POSITION IS ",ctr)
while(ctr<100): #runs the block of statements until the ctr value exceeds 100
    i=random.randint(1,6)#used to generate a random value
    j=input("PRESS ENTER TO ROLL THE DICE")
    print("NUMBER ON THE DICE IS ",i)
    ctr=ctr+i
    print("YOUR CURRENT POSITION IS ",ctr)
    if ctr==8: #checks if the position is at 8
        ctr=37 #moves the position to 37
        print("YOU CLIMBED THE LADDER FROM 8 TO 37")
    elif ctr==11: #checks if the position is at 11
        ctr=2 #moves the position to 2
        print("SNAKE BIT YOU..:( MOVE DOWN TO 2")
    elif ctr==25: #checks if the position is at 25
        ctr=4 #moves the position to 4
        print("SNAKE BIT YOU..:( MOVE DOWN TO 4")
    elif ctr==13: #checks if the position is at 13
        ctr=34 #moves the position to 34
        print("YOU CLIMBED THE LADDER FROM 13 TO 34")
    elif ctr==38: #checks if the position is at 38
        ctr=9 #moves the position to 9
        print("SNAKE BIT YOU..:( MOVE DOWN TO 9")
    elif ctr==40: #checks if the position is at 40
        ctr=68 #moves the position to 68
        print("YOU CLIMBED THE LADDER FROM 40 TO 68")
    elif ctr==52: #checks if the position is at 52
        ctr=81 #moves the position to 81
        print("YOU CLIMBED THE LADDER FROM 52 TO 81")
    elif ctr==65: #checks if the position is at 65
        ctr=46 #moves the position to 46
        print("SNAKE BIT YOU..:( MOVE DOWN TO 46")
    elif ctr==76: #checks if the position is at 76
        ctr=97 #moves the position to 97
        print("YOU CLIMBED THE LADDER FROM 76 TO 97")
    elif ctr==89: #checks if the position is at 89
        ctr=70 #moves the position to 70
        print("SNAKE BIT YOU..:( MOVE DOWN TO 70")
    elif ctr==93: #checks if the position is at 93
        ctr=64 #moves the position to 64
        print("SNAKE BIT YOU..:( MOVE DOWN TO 64")
    
print("YOU WON")

