import random

word_list = ["arvore", "bombom","chocolate"]

chosen_word = random.choice(word_list)

print(chosen_word)
display = []
word_length = len(chosen_word)
 
for _ in range(word_length):
    # or for n in chosen_word:
    display.append('"_"')
    # or display +="_"

print(display)

guess = input("Guess a letter: ").lower()
# range(len(chosen_word)) = will ran for many times we have letters in this word.
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)


# #When we send the "chosen_word" inside the "for", it will check letter by letter, even if i change the name of the varible.
# #chosen_word here is a word - str
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


