import turtle 

side_length= int(input("How long do you want the sides to be? "))
num_sides =int(input("How many sides do you want to have? "))

def drawEqSquare(mike, side_length, num_sides):
  for i in range(num_sides):
    mike.shape("turtle")
    mike.color("green")
    mike.forward(side_length)
    mike.left(360/num_sides)
    
mike = turtle.Turtle()
drawEqSquare(mike, side_length, num_sides)



