class StringUtility:
  def __init__(self, string):
    self.string = string

  def vowels(self):


    count = 0
    for i in self.string:
      if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count = count + 1
    if count > 4:
      return 'many'
    else:
      return str(count)

  def bothEnds(self):

    string_length = len(self.string)
    if string_length > 2:
      new_string = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    else:
      new_string = ''
    return new_string

  def fixStart(self):

    string_length = len(self.string)
    if string_length > 1:
      letter = self.string[0]
     
      new_string = ""
      x = 0    
      for i in self.string:
        if i == letter and x != 0:
          new_string = new_string + '*'
        else:
          new_string = new_string + i
        x = x + 1
      return new_string
    else:
      return self.string

  def asciiSum(self):

    num = []
    for i in range(len(self.string)):
      num.append(ord(self.string[i]))
    return sum(num)

  def cipher(self):

    letter = ''
    length = len(self.string)
    new_string = ''
    for i in self.string:
      if i.isupper() == False:
        if i == " ":
          new_string = new_string + i
        else:
          value = ord(i)
          index = ord(i) - ord('a')
          new_index = (index + length) % 26
          new_value = new_index + ord('a')
          new_char = chr(new_value)
          new_string = new_string + new_char
      else:
        value = ord(i)
        index = ord(i) - ord('A')
        new_index = (index + length) % 26
        new_value = new_index + ord('A')
        new_char = chr(new_value)
        new_string = new_string + new_char
    return new_string


  def __str__(self):
 
    return self.string
    
        
      
    
      
     

    
    
