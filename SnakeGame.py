from turtle import Turtle,Screen
import time
import random

class Snake:
  def __init__(self):
    self.positions=[0.00,-20.00,-40.00]
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
    self.new_segment=[]

  def create_snake(self):
    for pos in self.positions:
      self.add_segment(pos)

  def add_segment(self,position):
      new_segment=Turtle(shape="square")
      new_segment.penup()
      #new_segment.goto(position)
      new_segment.color("White")
      self.segments.append(new_segment)

  def extend(self):
      self.add_segment(self.segments[-1].position())

  def move_snake(self):
    for seq_no in range(len(self.segments)-1,0,-1):
      x_coordinate=self.segments[seq_no-1].xcor()
      y_coordinate=self.segments[seq_no-1].ycor()
      self.segments[seq_no].penup()
      self.segments[seq_no].goto(x_coordinate,y_coordinate)
    self.segments[0].penup()
    self.segments[0].forward(20)

  def up(self):
    if self.segments[0].heading()!=270:
      self.segments[0].setheading(90)

  def down(self):
    if self.segments[0].heading()!=90:
      self.segments[0].setheading(270)

  def left(self):
    if self.segments[0].heading()!=0:
      self.segments[0].setheading(180)

  def right(self):
    if self.segments[0].heading()!=180:
      self.segments[0].setheading(0)

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
  
    self.refresh()
    
  def refresh(self):
    random_x=random.randint(-200,200)
    random_y=random.randint(-200,200)
    self.goto(random_x,random_y)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    self.color("White")
    self.penup()
    self.goto(0,270)
    self.write(f"Score: {self.score}" , align="center", font=("Arial", 24,"normal"))
    self.hideturtle()

  def increase_score(self):
    self.score+=1
    self.clear()
    self.write(f"Score: {self.score}" , align="center", font=("Arial", 24,"normal"))

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER" , align="center", font=("Arial", 24,"normal"))


screen=Screen()
screen.setup(width=500,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

foodobj=Food()
snake=Snake()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameover=True 

while gameover:
  screen.update()
  time.sleep(0.2)
  snake.move_snake()
  if snake.head.distance(foodobj) < 15:
    foodobj.refresh()
    snake.extend()
    score.increase_score()
  if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()> 280 or snake.head.ycor()<-280:
    score.game_over()
    gameover=False
    
  for segment in snake.segments[1:]:
    if snake.head==segment:
      pass
    elif snake.head.distance(segment) < 10:
      score.game_over()
      gameover=False
      
score.game_over()

screen.exitonclick()
