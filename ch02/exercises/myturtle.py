import turtle
my_turtle =turtle.Turtle()
my_turtle.shape ("turtle")
my_turtle.color ("purple")
length =50
my_turtle.fillcolor("purple")
my_turtle.begin_fill()
my_turtle.forward (length)
my_turtle.right(90)
my_turtle.forward(length)
my_turtle.right(90)
my_turtle.forward(length)
my_turtle.right(90)
my_turtle.forward(length)
my_turtle.right(90)
my_turtle.end_fill()
turtle.done

#create new blue square

my_turtle.penup()
my_turtle.left(180)
my_turtle.forward(100)
my_turtle.pendown()
my_turtle.color("blue")
my_turtle.right(90)
my_turtle.forward (length)
my_turtle.right(90)
my_turtle.forward (length)
my_turtle.right(90)
my_turtle.forward (length)
my_turtle.right(90)
my_turtle.forward (length)
my_turtle.right(90)
turtle.done()

