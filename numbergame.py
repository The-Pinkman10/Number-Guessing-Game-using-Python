import random

print("Let's start our number guessing game..!!!\n\n")
print("Guess the  number I am thinking sir. Between 1-100 !\n")
guess=random.randint(1,101);
print("Enter the number you are guessing : \n")

while True:
    x=int(input())
    if x>guess:
        print("Go lower sir!")
    elif x<guess:
        print("Go higher sir!")
    else:
        print("You guessed the right number sir!")