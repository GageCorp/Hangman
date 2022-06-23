import random
from hangman_art import logo, stages
import hangman_words

#Triggers game end when True
end_of_game = False

#Guess amount
lives = 6

#Randomly selects word 
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
print(logo)

# Creates Dashes for the length of chosen word
display = []
for letter in chosen_word:
    display.append("_")

# Guessing loop until win or death
while end_of_game == False:
    print(f"{' '.join(display)}")
    guess = input("Guess a letter.").lower()
    if guess in display:
        print (f"You have already guessed {guess}.")
 
    #Fills in display with correctly guessed letters
    for x, letter in enumerate(chosen_word):
        if letter == guess:
            display[x] = guess

    # Reduces lives on incorrect guess
    if not guess in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word.")
        #Lose condition
        if lives == 0:
           
            print("You lose.")
            end_of_game = True
    # win condition
    if not "_" in display:
        print("You win!")
        end_of_game = True

    # Displays Hangmans current state
    print(stages[lives])