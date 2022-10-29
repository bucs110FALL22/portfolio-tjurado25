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
scale = 5 

pygame.init()
display = pygame.display.set_mode()
display.fill("red")
font = pygame.font.Font(None, 35)
pygame.display.flip()

for n in range(2, upper_limit + 1):
  count += 1
  if (n % 2) == 0:
    n = n // 2
  else:
    n = n * 3 + 1
    iters[n] = count
    print(iters)
    iters_graph = iters, count 



iters[max_val * scale] = count * scale

coordinates = list(iters.items())

if len(coordinates) > 1:
  values = pygame.draw.lines(display, "blue", False, coordinates)
  display.blit(pygame.transform.flip(display, False, True), (0, 0))

if count > max_so_far:
  max_value = max_so_far
  max_so_far = count

msg = font.render(f"(max_val) iterations", True, "Orange")
display.blit(msg, (scale, scale))

pygame.display.flip()


  
  
  





    
  
  
  


  