import random 
number = random.randint(1,9)
chances=0
print("guess the number between 1 and 9")
while chances <3:
    guess=int(input("enter your guess: "))
    if guess==number:
        print("You won!")
        break
    chances=chances+1

if chances==3:
    print("chances are over better luck next time.the correct number is ", number)