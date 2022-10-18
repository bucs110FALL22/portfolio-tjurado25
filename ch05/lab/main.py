import pygame

Scale =5
limit= 100
iters={}
max_so_far= 0
max_val=0

pygame.init()
display =pygame.display.set_mode()
font= pygame.font.Font(None, 42)

for val in range(2, limit+1):
  display.fill("white")
  count=0
  n= val

  while(n !=1):
    print(n)
    if (n % 2) ==0:
      n = n//2
    else:
      n = n * 3 + 1
    count = count +1
    

  iters[val * scale] = count * scale
  coordinates =list(iters.items())
  if len(coordinates)>1:
    value=pygame.draw.lines(display, "blue", False, coordinates)
    display.blit(pygame.transform.flip(display, False, True), (0, 0))

  if count > max_so_far:
    max_val = val
    max_so_far = count
  msg = font.render(f"max_val"):(max_so_far) iterations", True, "orange")
  display.blit(msg, (Scale, Scale))

  pygame.time.wait(50)
  pygame.display.flip()

  
  

                



               
