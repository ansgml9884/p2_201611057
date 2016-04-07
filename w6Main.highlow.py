def HighLowGame():
	import random
	guessesTaken = 0
	print ('Welcome! What is your name?')
	myname = raw_input()
	number = random.randint(1,300)
	print ('Well,'+myname+',I am thinking of a number between 1 and 300.')
	while guessesTaken < 100:
	    print('Take a guess.')
	    guess = input()
	    guess = int(guess)
	    guessesTaken =  guessesTaken + 1
	    if guess < number:
	        print('Your guess is too low.') 
	    if guess > number:
	        print('Your guess is too high.')
	    if guess==number:
	        print("That's right.")
	        break
	if guess == number:
	    guessesTaken = str(guessesTaken)
	    print('Good job,'+myName+'! You guessed my number in' +guesses-Taken +'guesses!') 

	if guess !=number:
	    number = str(number)
	    print('Nope. The number I was thinking of was '+number)


def lab6():
	HighLowGame()

def main():
	lab6()

if __name__=="__main__":
	main()
