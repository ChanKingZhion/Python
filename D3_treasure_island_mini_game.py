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

# FLOW CHART 👇
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first = input(
    "You reach a cross road. Where do you want to go? left or right?\n--> ")
if first.lower() != "left":
    print("\nYou fall into a hole. Game Over.")
else:
    second = input(
        '\nYou come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim to swim across.\n--> '
    )
    if second.lower() != "wait":
        print("\nYou attacked by sakana. Game Over.")
    else:
        third = input(
            "\nYou arrived at the island safely. There is a house with 3 doors. One red, one blue and one yellow. Which color do you choose?\n--> "
        )
        if third.lower() == "red":
            print("\nIt's a room full of fire. Game Over.")
        elif third.lower() == "blue":
            print("\nYou are eaten by a beast in the room. Game Over.")
        elif third.lower() == "yellow":
            print("\nYou found the treasure!!! You Win.")
        else:
            print("\nWhere are you going? See you. Game Over.")
