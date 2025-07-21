
I=int(input("guess my number from 1-10"))

while I!=6:
 if I<6:
  print("Ah you're lower.")
 elif I>6:
  print("Ah you're higher")
 I = int(input("Try again"))

 
print("CONGRATS!!. you got it the correct number IS 6 ")

#while searching for this ode i discovered the import function of random and down here is a better variable version
import random
I= random.randint(1,10)
Guess = input("guess a number from 1-10")

while Guess!=I:
 if Guess<I:
  print("Ah you're lower.")
 elif Guess>I:
  print("Ah you're higher")
 Guess = int(input("Try again"))

 
print("CONGRATS!!. you got it the correct number IS 6 ")