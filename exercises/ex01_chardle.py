"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730670557"

chardle_word = input(str("Enter a 5 character word: "))
if len(chardle_word) != 5:
    print("Error: the word has to be 5 letters")
    exit()
character = input(str("Enter a single character: "))
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + chardle_word)
if chardle_word[0] == character:
    print(character + " found at index 0")
if chardle_word[1] == character:
    print(character + " found at index 1")
if chardle_word[2] == character:
    print(character + " found at index 2")
if chardle_word[3] == character:
    print(character + " found at index 3")
if chardle_word[4] == character:
    print(character + " found at index 4")
counter = 0
if chardle_word[0] == character:
    counter = counter + 1
if chardle_word[1] == character:
    counter = counter + 1
if chardle_word[2] == character:
    counter = counter + 1
if chardle_word[3] == character:
    counter = counter + 1
if chardle_word[4] == character:
    counter = counter + 1

if counter == 0:
    print("No instances of " + character + " found in " + chardle_word)
if counter == 1:
    print("1 instance of " + character + " found in " + chardle_word)
if counter == 2: 
    print("2 instances of " + character + " found in " + chardle_word)
if counter == 3: 
    print("3 instances of " + character + " found in " + chardle_word)
if counter == 4: 
    print("4 instances of " + character + " found in " + chardle_word)
if counter == 5: 
    print("5 instances of " + character + " found in " + chardle_word)
