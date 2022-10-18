def percentage_to_letter(score=0):
  if score >= 90:
    print("A")
  if score >=80 and score < 90:
    print("B")
  if score >= 70 and score <80:
    print("C")
  if score >=60 and score <70:
    print("D")
  if score <=59:
    print("F")
      
  

#2nd function
def is_passing(letter=None):
  if letter in("A", "B", "C"):
    return True 
  else:
    return False 

Score = float(input("Please enter your grade: "))
percentage_to_letter(Score)
result = (percentage_to_letter)
is_passing (result)
                    


  


  

    