attempts = 1
import os
 
def main():
	secretNum = input("WHAT IS THE SECRET NUMBER: ")    
	os.system('cls')
	theGuess(secretNum)     
def theGuess(secretNum):
	theirGuess = input("\nENTER A GUESS: ")
	if theirGuess == secretNum:
		print("\nCONGRATS THE NUMBER %d WAS CORRECT\nYOU WIN!!!!") % (secretNum)        
		return
	elif theirGuess != secretNum and attempts < 6:
		if theirGuess > secretNum:
			print("\nTHE SECRET NUMBER IS LESS THAN %d") % (theirGuess)
		elif theirGuess < secretNum and attempts < 6:
			print("\nTHE SECRET NUMBER IS GREATER THAN %d") % (theirGuess)
	global attempts            
	attempts = attempts + 1        
	if attempts > 5:
		print("\nSORRY YOU ARE OUT OF GUESSES, THE NUMBER WAS %d") % (secretNum)       
		return	        
	theGuess(secretNum)            
main()