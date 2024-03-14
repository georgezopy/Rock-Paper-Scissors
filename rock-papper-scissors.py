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

import random

game = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
human = int(user_choice)

if user_choice >= 3 or user_choice < 0:
  print ("You typed an invalid number, try again!")
else:
  if human == 0:
      print(rock)
      print("You choose rock!")
  elif human == 1:
      print(paper)
      print("You choose paper!")
  else:
      print(scissors)
      print("You choose scissors!")
  
  computer = random.randint(0, 2)
  
  if computer == 0:
      print(rock)
      print("Computer choose rock!")
  elif computer == 1:
      print(paper)
      print("Computer choose paper!")
  else:
      print(scissors)
      print("Computer choose scissors!")
  
  print("\n")
  
  if human == 0 and computer == 1:
      print("You lose!")
  elif human == 0 and computer == 2:
      print("You win!")
  elif human == 1 and computer == 0:
      print("You win!")
  elif human == 1 and computer == 2:
      print("You lose!")
  elif human == 2 and computer == 0:
      print("You lose!")
  elif human == 2 and computer == 1:
      print("You win!")
  else:
      print("Draw!")
