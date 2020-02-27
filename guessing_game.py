import random
#prompts the user to enter the secret word
guess_word=input("Enter your secret word: ")
guess=""
guess_count=0

#prommpts the user to enter the limit of the guess
guess_limit= int(input("Enter the limit of the guess: "))

#a boolean to check if the user is out of guesses
out_of_guesses= False

while guess!= guess_word and not(out_of_guesses):
    if guess_count< guess_limit:
        guess=input("Enter your guess word: ")
        guess_count +=1
    else:
            out_of_guesses= True
if out_of_guesses:
    print("You have ran out of guesses, You lose")

else:
    
    print("You win")
    
