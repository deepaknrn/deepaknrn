#Rock Paper Sciccors Game

import random #import the random module

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice=random.randint(0,2)

rock='''---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor='''---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

images=[rock,paper,scissor]

print("You Choose \n")
print(images[user_choice])

print("Computer Choose \n")
print(images[computer_choice])

print("\n\n")

if user_choice==computer_choice:
  print("Draw")
elif user_choice==0 and computer_choice==2:
  print("You Win")
elif user_choice==1 and computer_choice==0:
  print("You Win")
elif user_choice==2 and computer_choice==1:
  print("You Win")
else:
  print("You Loose")
