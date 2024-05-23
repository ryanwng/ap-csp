import random
import math
guess_list = []
win = False
attempts = 0


print("Hello, welcome to the Number Guessing Game! To begin, state what range you want to guess from")
firstrange = int(input("First number "))
secondrange = int(input("Last number (inclusive!) "))

while secondrange < firstrange:
  print(f"The second number has to be greater than the first number, input a number greater than {firstrange}!")
  firstrange = int(input("First Number "))
  secondrange = int(input("Last number (inclusive!) " ))

correctnum = random.randint(firstrange,secondrange)
diff = secondrange-firstrange

attempts = int(round(math.log(diff,2)+2,0))

print(f"Okay, let's begin! Guess a number from {firstrange} to {secondrange}")
print(f"You will have {attempts} attempts")

def guess_and_answer(guess,part): #Two parts of the funct, one to determine if the guess has been guessed and another to determine if that guess is the correct num
  correct = False
  length = len(guess_list)
  if firstpart == True:
    for i in range(length):
      if guess_list[i] == guess:
        correct = True
  elif firstpart == False:
    if guess == correctnum:
      correct = True
    else:
      correct = False
  return(correct)

while win == False and attempts != 0:

  guess = int(input()) #Inputs guess
  firstpart = True
  
  if guess_and_answer(guess,firstpart) == True:
    print("You already guessed that! Please choose a number that is not from this list:")
    print(*guess_list)

  elif guess < firstrange or guess > secondrange:
    print(f"That's not a guessable number! Guess from {firstrange} to {secondrange}")
  
  else:
    attempts-=1
    guess_list.append(guess) #Adds guess to list
    guess_list.sort() #sorts list for convenience to the user
    firstpart = False
    
    if guess_and_answer(guess,firstpart) == True:
      print(f"Nice job! You guessed the number with {attempts} attempts left!")
      win = True
  
    elif guess_and_answer(guess,firstpart) == False:
      print("Nice try! But that's not the answer")
      if guess > correctnum:
        print("Your guess is higher than the answer")
      else:
        print("Your guess is lower than the answer")
      print(f"You have {attempts} attempts left")


if attempts == 0 and win == False:
  print("Nice try, but you didn't guess the number in time")
  print(f"The secret number was {correctnum}")
  print("Maybe you could use binary search next time...")
