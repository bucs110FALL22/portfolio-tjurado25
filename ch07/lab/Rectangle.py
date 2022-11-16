class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.height < 0:
      self.height = 0
    if self.width < 0:
      self.width = 0


    def __str__(self):
      return str("x: ", self.x, "y: ", self.y,"height: ", self.height, "width: ", self.width)
    
  
  
  

  
  

    
    
    