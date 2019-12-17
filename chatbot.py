import random
print("YOU ARE GOING TO TEST THIS CHATBOT!")
print("Do you like the movie Big Hero 6?")
test1 = input("Use 1 for yes and 0 for no: ")

if (test1 == 1):
	print("\nYou're officially a loser. Leave and never return.\n")

else:
	print("Move on my bretheren, for we shall have VICTORY\n\n")
	print("\nWhat is the longest possible distance you could walk on earth?")
	print("10m     13,910 miles     No     100,000,000,000km")
	print("1, 2, 3, or 4")
	dist = input("Enter the number of the answer: ")
	if (dist == 2):
		print("Correct. Finally you did something useful.")
		print("\nNext question.")
		print("\nWhat is the Krabby Patty secret formula?")
		print("Chocolate chunks     Plankton       Kelp       Cocaine")
		scrt = input("Enter the number: ")
		if (scrt == 4):
			print("Correct. Why else does everyone go back?")
			print("\nNext question.")
			print("\nHow does dragonfruit taste?")
			print("Spicy     Bland     Like chicken     Steel wool")
			taste = input("Enter the number: ")
			if (taste == 2):
				print("It should be spicy, but it's not.")
				print("\nFinal question.")
				print("\nWhere do Santa's letters actually go?")
				print("The South Pole      Your house     A toilet paper company     Donald Trump")
				place = input("Enter the number: ") 
				if (place == 2):
					print("Congradulations! You have successfully failed!")
				
				else:
					answers = [
						"Task failed successfully!",
						"Go eat a waffle and don't come back.",
					]
					print random.choice(answers)
				
			else:
				print("Go buy some and taste it.")
			
		else:
			print("Have you ever eaten the heavenly taste of a Krabby patty?")
	else:
		print("Go take that long walk off a short pier and hug an octopus.")
