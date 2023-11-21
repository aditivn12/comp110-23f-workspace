def char_exist(wordle_letter, secret_word):
    assert len(wordle_letter) == 1
    i = 0
    while i < len(secret_word):
        if secret_word[i] == wordle_letter:
            return True
        i+=1
    return False 

secret_word = "python"
wordle = input("What is your six letter word guess?: ")
j = 0
while j < len(wordle):
    print(wordle[j] + " exists: " + str(char_exist(wordle[j], secret_word)))
    j += 1


def emojified(guess: str, secret: str) -> str:
    char_exist
    assert len(guess) == len(secret)


