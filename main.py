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

option1 = input("You're at a crossroad, where do you want to go? Type \"Left\" or \"Right\" ").lower()

if option1 == "left":
    option2 = input("You've come to a lake. There is an island in the middle. Type \'Swim\' to swim across."
                    " Type \'Wait\' to wait ").lower()
    if option2 == "swim":
        print("You got attached by an angry trout. Game Over")
    else:
        option3 = input("You arrive at the island unharmed. There is a house with 3 doors. Blue, Red, or Yellow,"
                        " which one do you choose? ").lower()
        if (option3 == "blue") or (option3 == "red"):
            print("You were attacked by an assassin. Game Over")
        else:
            print("You found the treasure. You Win!")
elif option1 == "right":
    print("You fell into a hole. Game Over")
else:
    print("Wrong option. Good bye")