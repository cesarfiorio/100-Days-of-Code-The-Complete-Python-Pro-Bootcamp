import random

def start_the_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking in a number between 1 and 100")
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_level == "easy":
        game_dif(5)
    else:
        game_dif(10)

def game_dif(level):
    number = random.randint(1,100)
    guess_number = []
    print(number)
    while len(guess_number) < level:
        print (f"You have {level - (len(guess_number))} attempts remaining to guess the number.")
        print(len(guess_number))
        guess = int(input("Make a guess: "))
        guess_number.append(guess)
        if guess > number:
            print("Too high.")
            if len(guess_number) == 5:
                print("You lost")
        elif guess < number:
            print("Too Low.")
            if len(guess_number) == 5:
                print("You lost")
        elif guess == number:
            print("You own!")
            if len(guess_number) == 5:
                print("You lost")

start_the_game()