import turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
screen=turtle.Screen()
my_turtle.color("blue")
sides =int(input("How many sides do you want for the turtle:"))
length =int(input("How long do you want the sides to be:"))

angle =360/sides
for i in [angle]*sides:
  my_turtle.right(i)
  my_turtle.forward(length)
screen.exitonclick()