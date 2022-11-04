import random
from time import sleep as sp

print("Let's play a guessing game.\nI'm thinking of a number between 1 - 16.\n")

x = random.randint(1,17)

sp(2) # Sleep for 2 seconds

print("I have thought of a number 😅️!")

while True:
	
	user_guess = input("Can you guess the number : ")
	
	valid_guess = int(user_guess)
	
	if valid_guess > x:
		print("That number is too high!")
		
	elif valid_guess < x:
		print("That number is too less!")
		
	else:
		break

print("You have guessed correctly!")

