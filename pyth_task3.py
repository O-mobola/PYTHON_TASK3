#intro to the game
from random import randint

print("This game has 3 levels:\n")

levels = ["easy", "medium", "hard"]
for items in levels:
	print(f"{items}\n")

print("Enter EASY for easy mode, MEDIUM for medium mode, and HARD for hard mode.\n")
	
levelEasy = "easy"
levelMedium = "medium"
levelHard = "hard"

while True:
	select= input("Enter Your Level (easy, medium or hard): ")
	if select.lower() == levelEasy:
		
#easy mode selection		
		def easy():
			print("\nThis is the easy mode of the game.\nYou have 6 rounds to guess your secret number from (1-10).\nGood luck!\n")
			secretNum = randint(1,10)
			guessLimit = 6
			
			while guessLimit > 0:
				guess = int(input("Your guess: "))
				guessLimit -= 1
				
				if guess < 1 or guess > 10:
					print("enter between 1 and 10")
					
				if guess == secretNum:
					print("You Won!")
					break
		    			    
				elif guess !=secretNum:
					print("You guess wrong")
					print(f"You have {guessLimit} guess left")
				
				
					
		
		easy()
		
#medium mode selection		
	if select.lower() == levelMedium:
			
		def medium():
			print("\nThis is the medium mode of the game.\nYou have 4 rounds to guess your secret number from (1-20).\nGood luck!\n")
			secretNum = randint(1,20)
			guessLimit = 4
				
			while guessLimit > 0:
				guess = int(input("Your guess: "))
				guessLimit -= 1	
				
				if guess < 1 or guess > 20:
					print("enter between 1 and 20")
					
				if guess == secretNum:
					print("You Won!")
					break
			    			    
				elif guess !=secretNum:
					print("You guess wrong")
					print(f"You have {guessLimit} guess left")	
		
		
		medium()

#hard mode selection		
	if select.lower() == levelHard:
			
		def hard():
			print("\nThis is the hard mode of the game.\nYou have 3 rounds to guess your secret number from (1-50).\nGood luck!\n")
			secretNum = randint(1,50)
			guessLimit = 3
				
			while guessLimit > 0:
				guess = int(input("Your guess: "))
				guessLimit -= 1	
				
				if guess < 1 or guess > 50:
					print("enter between 1 and 50")
					
				if guess == secretNum:
					print("You Won!")
					break
		    
				elif guess !=secretNum:
					print("You guess wrong")
					print(f"You have {guessLimit} guess left")	
		
		hard()
#loop end		
	print("Game Over!")	
	break				