import random
import sys
list1=["rock","paper","scissor"]


while (True):
    computer=list1[random.randint(0,2)]

    computer1=computer[0]
    player=input("rock,paper,scissor?")
    player=player[0]
    player=player.lower()
    
    if(player==computer1):
        print("computer chose:",computer)
        print("It's a tie")
        
        
    elif player=="r":
        if computer1=="p":
            print("computer chose:",computer)
            print("You lose!!Don't worry...Try Again")
        else:
            print("computer chose:",computer)
            print("You win...You beat the machine")
    elif player=="p":
        if computer1=="s":
            print("computer chose:",computer)
            print("You lose!!Don't worry...Try Again")
        else:
            print("computer chose:",computer)
            print("You win...You beat the machine")
    elif player=="s":
        if computer1=="r":
            print("computer chose:",computer)
            print("You lose!!Don't worry...Try Again")
        else:
            print("computer chose:",computer)
            print("You win...You beat the machine")
    elif player=="q":
        print("You Quitting the game ;-(...Bye bye")
        sys.exit(0)
    else:
        print("Wrong credentials!!Try Again")

    
        
    
        
            
        
            
    
        
            
        
            
    
        
            
        
            
    
        
    
        
    
    
    


