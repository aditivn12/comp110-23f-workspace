"""ex02_one_shot_wordle!"""
__author__ = "730670557"
secret_word = "python"
# This is the input for the six letter guess 
wordle = input("What is your six letter word guess?: ")
# This is to see if the length is the same for the secret word and the guess
while len(wordle) != len(secret_word):
    wordle = input("That was not 6 letters! Try again: ")
# This is the output if the guess and the word are not the same
if wordle != secret_word:
    print("Not quite. Play again soon!")
# This is the output if the word and the guess are the same. 
if wordle == secret_word:
    print("Woo! You got it!")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# These are variables that the code uses to iterate through the secret word and the guess and also to output the green, yellow, and white box. 
count = 0
output = ""
character = False
count_exists = 0
# This checks to see if a character at an index of the guess and the secret word is the same and if it is then the green box shows.  
while count < len(secret_word):
    if (wordle[count] == secret_word[count]):
        output += GREEN_BOX
    else:
        # This checks the yellow box condition and the while loop runs until it finds a character in the secret word and the guess to be the same and if it is it turns the variable character true.
        while count_exists < len(secret_word):
            if wordle[count] == secret_word[count_exists]:
                character = True 
            count_exists += 1 
        # When the varaible character is true the yellow box shows
        if character is True:
            output += YELLOW_BOX
        # When the variable character is false the white box shows
        if character is False: 
            output += WHITE_BOX
        # This resets the count and character variable back to false
        character = False
        count_exists = 0
    # This adds one to count so that the code can go to the next character of the guess. 
    count += 1     
print(output)