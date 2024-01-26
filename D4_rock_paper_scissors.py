import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
loop = True
while(loop):
  try:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if choice >= 0 and choice < len(list):
      loop = False
      pc_choice = random.randint(0, 2)
      print(f"You choose:{list[choice]}")
      print(f"Computer choose:{list[pc_choice]}")
      if choice - pc_choice == 0:
          print("Draw")
      elif choice - pc_choice == -1 or choice - pc_choice == 2:
          print("Computer Wins")
      elif choice - pc_choice == 1 or choice - pc_choice == -2:
          print("You Win")
    else:
      print("Try Again")
  except:
    print("Try Again")
