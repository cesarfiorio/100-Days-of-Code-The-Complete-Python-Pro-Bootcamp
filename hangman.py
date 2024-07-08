import random

word_list = ["arvore", "bombom","chocolate"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

#When we send the "chosen_word" inside the "for", it will check letter by letter, even if i change the name of the varible.
#chosen_word her eis a word - str
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#When we send the "chosen_word" inside the "for", it will check letter by letter, even if i change the name of the varible.
#chosen_word her eis a word - str
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
