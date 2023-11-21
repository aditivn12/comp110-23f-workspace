"""exercise 3 wordle assignment"""
__author__ = "730670557"

def contains_char(searching_for_word: str, searching_for_character: str) -> bool:
    assert len(searching_for_character) == 1
    i = 0
    while i < len(searching_for_word):
        if searching_for_word[i] == searching_for_character:
            return True
        i+=1        
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess_word: str, secret: str) -> str:
    assert len(guess_word) == len(secret)  
    g = 0
    return_emoji = ""
    while g < len(guess_word):
        if guess_word[g] == secret[g]:
            return_emoji += GREEN_BOX
        elif contains_char(secret, guess_word[g]):
            return_emoji += YELLOW_BOX
        else: 
            return_emoji += WHITE_BOX
        g += 1
    return return_emoji


def input_guess(length: int) -> str:
    wordle = input("What is your " + str(length) + " letter guess?: ")
    while len(wordle) != length:
            wordle = input("That wasn't " + str(length) + " letters! Try again: ")   
    return wordle

def main() -> None:
    secret_word: str = "python"
    max_turns = 6
    turns = 0
    while turns < max_turns:
        turns += 1
        print("=== Turn " + str(turns) + "/" + str(max_turns) + " ===")
        wordle = input_guess(len(secret_word))
        result = emojified(wordle, secret_word)
        print(result)
        if wordle == secret_word:
            print("You won in " + str(turns) + "/" + str(max_turns) + " turns!")
            break
    else:
        print("X/" + str(max_turns) + " - Sorry, try again!")

if __name__ == "__main__":
    main()