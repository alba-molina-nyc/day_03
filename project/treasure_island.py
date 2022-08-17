def treasure_island():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    direction = input('do you wish to go LEFT or do you wish to go RIGHT? : ').lower()
    # decision = input('do you wish to SWIM or to WAIT? : ').lower()
    # door = input('do you choose the RED door, the BLUE door or the YELLOW door? : ').lower()
    
    if direction == 'left':
        print(f'going {direction}')
        decision = input('do you wish to SWIM or to WAIT? : ').lower()
        if decision == 'swim':
            print(f'attacked by trout, game over {decision}')
        elif decision == 'wait':
            door = input('do you choose the RED door, the BLUE door or the YELLOW door? : ').lower()
            if door == 'yellow':
                print('you win!{door}')
            elif door == 'red':
                print('burned by fire you LOSE{door}')
            else:
                print('game over')
 
    else:
        print('Game over')
   
    


                
if __name__ == '__main__':
    treasure_island()