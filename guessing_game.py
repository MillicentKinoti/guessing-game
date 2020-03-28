# Prompts the user to enter the secret word
guess_word = input("Enter your secret word: ")

# Prommpts the user to enter the limit of the guesses
# n is the placeholder for input type checking
n = input("Enter the limit of the guess (number): ")

# If n is not a number prompt until a number is entered
while n.isdigit() == False:
    n = input("Please enter a numeric input: ")
    
# Type convert the input
guess_limit = int(n)

#############################
## Using a While loop
#############################

# Keeps track of the number of guesses
guess_count = 0

# Variable to store the guessed word
guess = ""

# Boolean to check if the user is out of guesses
out_of_guesses = False

while guess != guess_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess=input("Enter your guess word: ")
        guess_count += 1
    else:
        out_of_guesses= True

if out_of_guesses:
    print("You have ran out of guesses, You lose")
else:
    print("You win")

#############################
## Using a For loop
#############################
#    
#for i in range(guess_limit):
#    guess = input("Enter your guess word: ")
#    if guess == guess_word:
#        print("You win")
#        break
#
#if guess != guess_word:
#    print("You have ran out of guesses, You lose")