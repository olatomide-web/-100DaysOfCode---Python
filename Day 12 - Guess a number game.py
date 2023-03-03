#import random to generate random number
import random


#define global scopes to use
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

#define function to check player's guess against the actual answer.
def check_answer(guess, number, turns):
    if guess > number:
        print("too high")
        return turns - 1
    elif guess < number:
        print("too low")
        return turns - 1
    else:
        print(f"you got it, the number was {number}")





#define a function to set the game's difficulty level
def set_difficulty():
    difficulty_level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
     
    number = random.randint(1, 100)

    print(f"the number is {number}")


    turns = set_difficulty()

    
    guess = 0
    #repeat the guessing game if they get it wrong
    while guess != number:
        print(f"You have {turns} attempt remaining")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, number, turns)

        if turns == 0:
            print("you have run out of guesses, you lose!")
            return
        elif guess != number:
            print("guess again")

guessing_game()







#import random module to generate random numbers
#conditions to meet
#choosing a random number between 1-100
#define a function to set the game's difficulty level
#let the player guess a number
#define another function to check player's guess against the actual answer
#track the number of turns and reduce by 1 each turn
#repeat the guessing game if they get it wrong
