def Leap():
    year=input("User input year : ")
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "Leap year"
    else:
        print "Not Leap year"
    wn = raw_input()

"""

@startuml
title Check leap year
start
:user input year;
if((year%4 == 0) and (year%100!=0 or year%400==0)) then (yes)
:print leap year;
else (no)
:print Not leap year;
endif
stop
@enduml

"""
def HighLowGame():
 	import random
	guessesTaken = 0
	print ('Welcome! What is your name?')
	myname = raw_input()
	number = random.randint(1,200)
	print ('Well,'+myname+',I am thinking of a number between 1 and 200.')
	while guessesTaken < 10:
	    print('Take a guess.')
	    guess = input()
	    guess = int(guess)
	    guessesTaken =  guessesTaken + 1
	    if guess < number:
	        print('Your guess is too low.') 
	    if guess > number:
	        print('Your guess is too high.')
            if guess==number:
                print('Right! Your guess is correct!(Just ignore the message below^^)')
 	if guess == number:
	    guessesTaken = str(guessesTaken)
	    print('Good job,'+myName+'! You guessed my number in' +guesses-Taken +'guesses!') 
	if guess !=number:
	    number = str(number)
	    print('Nope. The number I was thinking of was '+number)
        wn = raw_input()

"""

@startuml
start
title Let's Play High/Low Game
:n=set random number;
:your playing chance=a and input your number(=b);
while( )
if (not n=b) then (n<b)
: print Your guess is high;
else (n>b)
:print Your guess is low;
endif
endwhile
:chance is over or a=b;
if ( ) then (over chance)
:print Your guess is failed;
else (a=b)
:print Good! Your guess is correct!;
endif
:finish;
stop

"""


def lab6():
    Leap() 
    HighLowGame()   

def main():
    lab6()

if __name__=="__main__":
    main()

