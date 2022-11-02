num = 5
t = range(10)
mystr= "This is a string with a " + str(num) + " and " + str(t)
print(mystr)

print(f"This is another fstring: {1 > 0}")


class Graph:
  def __init__(self, title= "My Graph"):
    self.points = []
    self.title = title

  def add_point(self,p):
    self.points.append(p)

  def __str__(self):
    point_str = ""
    for p in self.points:
      point_str += f" {p.x}, {p.y})"
    return f"{self.title}: {point_str}"
  
  def main():
    g = Graph()
    print(g)
    p = Point(5, 2)
    p2 = Point(3, 4)
    g.add_point(p)
    g.add_point(p2)
    print(g)

  main()



  
    



  






     
                                 