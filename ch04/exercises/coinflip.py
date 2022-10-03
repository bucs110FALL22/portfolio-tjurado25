import turtle
import random 
turtle.screensize(500, 300 , bg="blue")
canvwidth = turtle.window_width()
canvheight = turtle.window_height()
turtle1=turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("black")
turtle1.setpos(0,0)

while abs(turtle1.xcor()) < (canvwidth/2) and abs (turtle1.ycor()) < (canvwidth/2):
  mylist = ["heads", "tails"]
  coinflip = random.choice(mylist)
  print(random.choice(mylist))
  if coinflip == "heads": 
    turtle1.left(90)
    turtle1.forward(50)
  elif coinflip == "tails":
    turtle1.right(90)
    turtle1.forward(50)
     




    

  
  
    
  



            