import pygame   
import random 
import math

pygame.init()
window = pygame.display.set_mode((300,300))
windowSize = pygame.display.get_window_size()
print(windowSize)
color1="blue"
color2="red"
center = (150, 150)
hitcount = 0
game = True

while game:
  pygame.display.flip()
  window.fill("orange")
  pygame.draw.circle(window, "crimson", (150, 150), 150, 0)
  pygame.draw.line(window, "black", (150,0), (150, 300))
  pygame.draw.line(window,"black", (0, 150), (300, 150))
  pygame.display.flip()

  for x in ["game"]*10:
    pygame.time.wait(1000)
    xcor = random.randrange(0, 300)
    ycor = random.randrange(0,300)
    distance_from_center = math.hypot((xcor-150), (ycor-150))
    is_in_circle = distance_from_center <= 150
    if is_in_circle:
      pygame.draw.circle(window, "orange", (xcor, ycor), 5, 0)
      pygame.display.flip()
      print("Hit!")
      hitcount +=1
    else:
      pygame.draw.circle(window, "white", (xcor, ycor), 5, 0)
      pygame.display.flip()
      print("Miss!")
  print(f"You completed the game! You landed {hitcount} darts on the board out of 10!")
  pygame.time.wait(2000)
  game = False

window.fill("black")
pygame.display.flip()
print("Click on the color of the player that you think will win the competition.")
selection = True

while selection:
  Rect1=((50, 175), (125, 50))
  Rect2= ((225, 175), (125, 50))
  hitboxwidth= 125
  hitboxheight=50
  redbuttonbox=pygame.Rect(Rect1)
  bluebuttonbox=pygame.Rect(Rect2)
  pygame.draw.rect(window, "red", Rect1)
  pygame.draw.rect(window, "blue", Rect2)
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type ==pygame.MOUSEBUTTONDOWN:
      mouseclickpos=event.pos
      if redbuttonbox.collidepoint(mouseclickpos):
        print("You have selected Player Red")
        pygame.time.wait(500)
        window.fill("black")
        playerchoice="red"
        selection = False
      elif bluebuttonbox.collidepoint(mouseclickpos):
        print("You have selected Player Blue")
        pygame.time.wait(500)
        window.fill("black")
        playerchoice = "blue"
        selection = False
        
versus = True
redhits=0
bluehits=0

while versus:
  pygame.display.flip()
  window.fill("orange")
  pygame.draw.circle(window, "crimson", (150, 150), 150, 0)
  pygame.draw.line(window, "black", (150,0), (150, 300))
  pygame.draw.line(window, "black", (0, 150), (300, 150))
  pygame.display.flip()
  for i in range(1, 11):
    print(f"ROUND {i}!")
    for _ in [color1, color2]:
      pygame.time.wait(1000)
      xcor = random.randrange(0,300)
      ycor= random.randrange(0,300)
      distance_from_center = math.hypot((xcor-150), ycor-150)
      is_in_circle=distance_from_center <=150
      if is_in_circle:
        pygame.draw.circle(window, _, (xcor, ycor), 5,0)
        pygame.display.flip()
        print(f"{_} gets a hit!")
        if _ ==color1:
          redhits +=1
        elif _ ==color2:
          bluehits +=1
      else:
        pygame.draw.circle(window, "white", (xcor, ycor), 5, 0)
        pygame.display.flip()
        print(f"{_} misses!")
  pygame.time.wait(2000)
  if redhits == bluehits:
    print(f"The game is a tie! Both players had {bluehits} points")
    versus =False
  elif redhits > bluehits:
    print(f"Player Red won the game with {redhits} points!")
    if playerchoice == "red":
      print("Your guess was correct. Play again?")
      versus=False
    else:
      print("Your guess was incorrect. Play again?")
      versus=False
  elif bluehits > redhits:
    print(f"Player Blue won the game with {bluehits} points")
    if playerchoice =="blue":
      print("Your guess was correct. Play again?")
      versus=False
    else:
      print("Your guess was incorrect. Play again?")
      versus=False
pygame.time.wait(3000)
    
    
    
    
    
    
  
    
        
        
                          
        
                          
  
  
      
  



  
    
  
          







    


  
    
      
    
    



