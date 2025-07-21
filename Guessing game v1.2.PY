import random
I= random.randint(1,10)
Guess = int(input("guess a number from 1-10"))

guess_count=0
guess_limit=4

while Guess!=I and guess_count<guess_limit-1:
 
 if Guess<I:
  print("Ah you're lower.")
  
 else:
  print("Ah you're higher")
  
 guess_count+= 1
 Guess = int(input("Try again"))
 
guess_count += 1

if Guess == I:
    print("CONGRATS!! You got it. The correct number is " + str(I))
else:
    print("Ah, sorry, you're out of tries. The number was " + str(I))

print("Total guesses used:", guess_count)