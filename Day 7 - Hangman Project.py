#import random to generate words from the list randomly
import random


from hangman_word_list import word_list


#Randomly choose a word from the word list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = 6
lives = 6


#import hangman logo

from hangman_art import logo
print(logo)

print(f'pssst, the solution is {chosen_word}')



#create an empty list called display
display = [ ]

#generate underscores(_) for the chosen_word using for loop
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
#print(display)



game_over = False
while game_over == False:
    #user should guess a number
    guess = input("Guess a letter:\n")

    #convert the guess to a lowercase letter
    guess = guess.lower()

    if guess in display:
        print(f"you have already guessed {guess}")
        

    for placement in range(len(chosen_word)):
        letter = chosen_word[placement]
        if letter == guess:
            display[placement] = letter

    print(display)

    if guess not in chosen_word:

        print(f"you guessed {guess}, that's not in the word. You lose a life")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")

    from hangman_art import stages
    print(stages[lives])

