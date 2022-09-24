import turtle #1. import modules
import random
import pygame
import math 


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
for i in range(1, 100)

michelangelo.speed(1)
leonardo.speed(2)

michelangelo.pendown()
leonardo.pendown()
michelangelo.forward(150)
leonardo.forward(150)




# PART B - complete part B here
pygame.init()
window = pygame.display.setmode()


for i in range(num_sides):
  theta = 2(2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  t_list = (x,y) 
  coords.append(t_list)

pygame.draw.polygon(surface, "gold", shape_points(3))
pygame.display.flip()
pygame.time.wait(200)
pygame.draw.polygon(surface, "green", shape_points(4))
pygame.display.flip()
pygame.time.wait(200)
pygame.draw.polygon(surface, "red", (shape_points(6))
pygame.display.flip()
pygame.time.wait(200)
pygame.draw.polygon(surface, "purple", shape_points(9))
window.fill("blue") 
pygame.display.flip()
            
              













window.exitonclick()
