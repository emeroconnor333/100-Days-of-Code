#rock, paper, scissors

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
userinput= input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

import random
compnum= random.randint(0,2)

if userinput== '0':
  print(rock)
  print("Computer chose:")
  if compnum== 0:
    print(rock)
    print("It's a draw!")
  if compnum== 1:
    print(paper)
    print("You lose!")
  if compnum== 2:
    print(scissors)
    print("You win!")

if userinput== '1':
  print(paper)
  print("Computer chose:")
  if compnum== 0:
    print(rock)
    print("You win!")
  if compnum== 1:
    print(paper)
    print("It's a draw!")
  if compnum== 2:
    print(scissors)
    print("You lose!")

else:
  print(scissors)
  print("Computer chose:")
  if compnum== 0:
    print(rock)
    print("You lose!")
  if compnum== 1:
    print(paper)
    print("You win!")
  if compnum== 2:
    print(scissors)
    print("It's a draw!")