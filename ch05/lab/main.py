import pygame

n=101

while n != 1:
  if (n % 2) == 0:
    n = n // 2
    print(n)
  else:
    n = n * 3 + 1
    print(n)

n = 101
count = 0

while n != 1:
  count += 1
  if (n % 2)== 0:
    n = n // 2
    print(n)
  else:
    n = n * 3 + 1
    print(n)
print("count:", count)

n=101
start = (n)
upper_limit = 20
iters = {}
count = 0
max_so_far = 0
max_val = 0

for start in range(2, upper_limit + 1):
  count += 1
  if (n % 2) == 0:
    n = n // 2
  else:
    n = n * 3 + 1
    iters[start] = count
    print(iters)

n=101
start = (n)
upper_limit = 20
iters = {}
count = 0
max_so_far = 0
scale = 10

pygame.init()
display_width = 300
display_height = 300
display = pygame.display.set_mode([display_width, display_height])
font = pygame.font.Font(None, 20)
pygame.display.flip()
color = "blue"
new_display = pygame.transform.flip(display, False, True)
display.fill([0, 255, 0])

for integer in range(2, upper_limit +1):
  count = 0 
  n = integer
  while n != 1:
    count += 1
    if n % 2 == 0:
      n = n / 2
    else:
      n = n * 3 +1 
  if count > max_so_far:
    max_so_far = count 
  iters[integer] = count
  coordinates = []
  if integer > 2:
    msg = font.render(f"{max_so_far}", True, "red")
    for iterItem in iters.items():
      coordinates.append((iterItem[0] * 7, iterItem[1] * 7))
    display.fill("black")
    pygame.draw.lines(display, "blue", False, (coordinates))
    new_graph = pygame.transform.flip(display, False, True)
    pygame.display.flip()
    display.blit(new_graph, (0, 0))
    display.blit(msg, (30, 100))
    pygame.display.flip()
    pygame.time.wait(100)
  pygame.time.wait(1000)    


    
  
      
  
  
  

