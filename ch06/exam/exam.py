import turtle
 
screen = turtle.Screen
panda = turtle.Turtle()
def ring(col, rad):
    panda.fillcolor(col)
    panda.begin_fill()
    panda.circle(rad)
    panda.end_fill()
 

#first ear
panda.up()
panda.setpos(-35, 95)
panda.down
ring('black', 15)
 
#second ear
panda.up()
panda.setpos(35, 95)
panda.down()
ring('black', 15)
 
#face
panda.up()
panda.setpos(0, 35)
panda.down()
ring('white', 40)
 
#black eyes 
 
#Draw first eye
panda.up()
panda.setpos(-18, 75)
panda.down
ring('black', 8)
 
#second eye
panda.up()
panda.setpos(18, 75)
panda.down()
ring('black', 8)

#Little white eye in black eye
#first eye
panda.up()
panda.setpos(-18, 77)
panda.down()
ring('white', 4)
 
#second eye.
panda.up()
panda.setpos(18, 77)
panda.down()
ring('white', 4)
 
#Draw nose 
panda.up()
panda.setpos(0, 55)
panda.down
ring('black', 5)
 
#mouth 
panda.up()
panda.setpos(0, 55)
panda.down()
panda.right(90)
panda.circle(5, 180)
panda.up()
panda.setpos(0, 55)
panda.down()
panda.left(360)
panda.circle(5, -180)
panda.hideturtle()

screen = turtle.Screen
screen.exitonclick()