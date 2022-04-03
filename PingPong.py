from turtle import Turtle,Screen 
import time
import random


#Setting up the Screen 
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

score_paddle1=0
score_paddle2=0

#Setting up Paddle

class Paddle(Turtle):
  def __init__(self,pos1,pos2):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.penup()
    self.goto(pos1,pos2)
    self.shapesize(stretch_len=1,stretch_wid=5)

  def right_up(self):
    self.goto(self.xcor(),self.ycor()+10)

  def right_down(self):
    self.goto(self.xcor(),self.ycor()-10)

  def left_up(self):
    self.goto(self.xcor(),self.ycor()+10)

  def left_down(self):
    self.goto(self.xcor(),self.ycor()-10)

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_move=10
    self.y_move=10
    
  def move(self):
    new_x=self.xcor()+self.x_move
    new_y=self.ycor()+self.y_move
    self.goto(new_x,new_y)

  def bounce_y(self):
    self.y_move *=-1

  def bounce_x(self):
    self.x_move *=-1    

  def reset_position(self):
    self.goto(0,0)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score=0
    self.r_score=0
    self.update_scoreboard()
  
  def update_scoreboard(self):
    self.goto(-100,220)
    self.write(self.l_score,move=False,font=('Arial', 30, 'normal'))
    self.goto(30,220)
    self.write(self.r_score,move=False,font=('Arial', 30, 'normal'))

  def increasepoint_paddle1(self):
    self.clear()
    self.r_score=self.r_score+1
    self.update_scoreboard()

  def increasepoint_paddle2(self):
    self.clear()
    self.l_score=self.l_score+1
    self.update_scoreboard()


paddle1=Paddle(350.00,0.00)
paddle2=Paddle(-350.00,0.00)
ball=Ball()
score=Scoreboard()

screen.listen()

screen.onkey(paddle1.right_up,"Up")
screen.onkey(paddle1.right_down,"Down")
screen.onkey(paddle2.left_up,"w")
screen.onkey(paddle2.left_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect collission with Wall
    if ball.ycor() > 280 or ball.ycor() < -125:
      ball.bounce_y() 
    
    #Detect collission with Right Paddle
    elif (ball.distance(paddle1) < 50 and ball.xcor() > 330) or (ball.distance(paddle2) < 50 and ball.xcor() < -330):
      ball.bounce_x()
    
    #Ball goes beyond , reset the Ball
    else:
      if ball.xcor() > 330 :
        score_paddle2=score_paddle2+1
        ball.reset_position()
        ball.bounce_x()
        score.increasepoint_paddle2()
      if ball.xcor() < -390 :
        score_paddle1=score_paddle1+1
        ball.reset_position()
        ball.bounce_x()
        score.increasepoint_paddle1()
        


screen.exitonclick()
