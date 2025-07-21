import random
Guess_count = 0
guess_limit = 4
I= random.randint(1,10)
while Guess_count<guess_limit:
     Guess= int(input("Guess a number from 1-10"))
     Guess_count += 1

     if  Guess == I:
         print("Congrats you got it !!")
         break
     elif Guess>I:
          print("lower")
     elif Guess<I:
          print("higher")
     
if Guess_count == guess_limit and Guess != I:
     print("Sorry youre out of tries")
else:
     print("Your guess count is  " + str(Guess_count) + " and the number is " + str(I))