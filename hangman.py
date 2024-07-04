import random

word_list = ["arvore", "bombom","chocolate"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

#When we send the "chosen_word" inside the "for", it will check letter by letter.
for n in chosen_word:
    if n == guess:
        print("Right")
    else:
        print("Wrong")
