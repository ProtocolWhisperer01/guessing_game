#############################################################################
## 									   ##
##	Title : Guessing Game						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# This is a simple guessing game program!

import random
from time import sleep as sp

print("Let's play a guessing game.\nI'm thinking of a number between 1 - 16.\n")

x = random.randint(1,17)

sp(1.5) # Sleep for 2 seconds

print("I have thought of a number 😅️!")
sp(3) 
print("Ooh! You have 4 attempts.\n")
attempts = 0
while True:
	try:
		if attempts != 4:
			attempts += 1
		else:
			break
		user_guess = input("Can you guess the number : ")
		valid_guess = int(user_guess)
		if valid_guess in range(1,17):
			if valid_guess > x:
				print("That number is too high!")
			elif valid_guess < x:
				print("That number is too less!")
			else:
				break
		else:
			print("That value is out of scope!")
	except:
		print("Enter a valid number!")

if valid_guess == x:
	print("You have guessed correctly!")
else:
	print("Sorry you are out of guesses.\nIt was ,", x)
