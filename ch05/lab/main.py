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
display.fill("red")
font = pygame.font.Font(None, 20)
pygame.display.flip()
color = "blue"
pos = (10,10)
new_display = pygame.transform.flip(display, False, True)
iters_new = {}
display.fill([0, 255, 0])

for n in range(2, upper_limit + 1):
  count += 1
  if (n % 2) == 0:
    n = n // 2
  else:
    n = n * 3 + 1
    iters[n] = count
    print(iters)
    

  

  iters_new[n * scale] = display_height-count*scale

  coordinates = list(iters_new.items())

  if count > max_so_far:
    max_so_far = count
    max_val = str(max_so_far)
    display.blit(new_display, (0,0))
    msg = font.render("Max value of iterations is "+ max_val, True, color)
  display.blit(msg, pos)

  if len(coordinates) > 1:
    pygame.draw.lines(display, color, False, coordinates)
    pygame.time.wait(1000)
    pygame.display.flip()

print(iters)
pygame.time.wait(1000)

