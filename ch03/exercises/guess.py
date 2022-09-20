import random
num = random.randrange(1, 11)

num_guesses = 0
correct_guess = False
for i in range(3):
  if not correct_guess:
    guess_num = int(input("Enter a number 1 through 10:"))
    num_guesses += 1
    if guess_num > num:
      print("Your number is too high")
    elif guess_num < num:
      print("Your number is too low")
    else:
      print("You guessed the number!")
      break
print("It took you" , num_guesses, "guesses")
  
  