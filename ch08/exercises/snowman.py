import pygame
import random

class Snowmen:

  def __init__(self,width,x,y):
    self.color = [
      random.randint(0, 255),
      random.randint(0, 255),
      random.int(0, 255),
    ]
    self.image = Surface((width, 175))
    self.rect = self.image.get_rect()
    






class Controller:

  def __init__(self):
    #need to set up all data for our program.
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.background = "Orange"
    
    number_of_snowpeople = 3
    size = pygame.display.get_window_size() #(width and height)
    width = size[0] / number_of_snowpeople
    
    self.snowpeoples = []
    xpos = 0
    for i in range(number_of_snowpeople):
      snowpeople.append(Snowman(xpos, 0))
      xpos += width 

  def mainloop():
    while True: #one time through this loop is one picture frame
      #1. Respond to events; no events - no event loop
      #2. Update your models. 
      for s in self.snowpeoples:
        s.update()

      self.screen.fill(self.background)
      #3. Draw models

      for s in self.snowpeoples:
        self.screen.blit(s.image, s.rect)
        
      #4. Display the screen
      pygame.display.flip()


    
        

    


def main():
  controller = Controller()
  controller.mainloop()

main()
  
    
  