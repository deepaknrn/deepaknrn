from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500,height=600)
import random

colours=["blue","green","yellow","orange","red"]
x=-250.00
y=[120.00,100.00,80.00,60.00,40.00]
speed=[1,2,3,4,5]
obj_list=[]

gameover=True

for turtle_index in range(len(colours)):
  tim=Turtle()
  tim.shape("turtle")
  tim.penup()
  tim.setposition(x,y[turtle_index])
  tim.color(colours[turtle_index])
  obj_list.append(tim)

user_bet=screen.textinput("Make your Bet","Who will win the race enter a color:")

def assign_speed(obj_list):
  v_speed=random.choice(speed)
  obj_list.speed=v_speed
  speed.remove(v_speed)
  return obj_list.speed

for turtle_index in range(len(colours)):
  obj_list[turtle_index].speed=assign_speed(obj_list[turtle_index])

def movements(obj_list):
  for turtle_index in range(len(colours)):
    obj_list[turtle_index].forward(obj_list[turtle_index].speed)

while gameover:    
  for turtle_index in range(len(colours)):
    movements(obj_list)
    if obj_list[turtle_index].xcor()>230:
      winner=obj_list[turtle_index].color()
      gameover=False

if user_bet==winner[0]:
  print("Congratulations You Won")
else:
  print("You Lost")
  

screen.exitonclick()
