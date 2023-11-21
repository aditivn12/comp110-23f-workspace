"""exercise 3 wordle assignment!"""
__author__ = "730670557"


# This function called contains_char and it looks for a character in a word and returns true if it is present and false if it isn't. 
def contains_char(searching_in_word: str, searching_for_character: str) -> bool:
    """This functions returns true or false based on if the character is in the word."""
    assert len(searching_for_character) == 1
    i: int = 0
    while i < len(searching_in_word):
        if searching_in_word[i] == searching_for_character:
            return True
        i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """This function prints the correct emoji based on the guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess_word) == len(secret_word)  
    g: int = 0
    return_emoji: str = ""
    # This part of the function checks if the character is at the same index as the word and if it is, it returns the green box. 
    while g < len(guess_word):
        if guess_word[g] == secret_word[g]:
            return_emoji += GREEN_BOX
        elif contains_char(secret_word, guess_word[g]):
            # This calls the contains_char function to see if a character in the guess is in the secret. If it is then it returns the yellow box otherwise it returns the white box. 
            return_emoji += YELLOW_BOX
        else: 
            return_emoji += WHITE_BOX
        g += 1
    return return_emoji


# This function is there for the user to input a guess. If the guess isn't the correct length, then it prompts the user to retry. 
def input_guess(length_of_word: int) -> str:
    """This allows the user to input a word."""
    wordle: str = input("Enter a " + str(length_of_word) + " character word: ")
    while len(wordle) != length_of_word:
        wordle = input("That wasn't " + str(length_of_word) + " chars! Try again: ")
    return wordle


# This function is there to put all the other functions together and also keep track of the turns the user takes. 
def main() -> None:
    """This function includes two other function and also keeps tracks of the user's turns."""
    secret_word: str = "codes"
    most_turns: int = 6
    turns: int = 1
    while turns <= most_turns:
        print("=== Turn " + str(turns) + "/" + str(most_turns) + " ===")
        # The functions are being used here. 
        wordle: str = input_guess(len(secret_word))
        emoji: str = emojified(wordle, secret_word)
        print(emoji)
        if wordle == secret_word:
            print("You won in " + str(turns) + "/" + str(most_turns) + " turns!")
            return
        turns += 1
    print("X/" + str(most_turns) + " - Sorry, try again!")


if __name__ == "__main__":
    main()