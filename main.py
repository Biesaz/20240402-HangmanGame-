import os
import random
import stages
import words

def clear_screen() -> None:
    os.system('cls')

clear_screen()

attempts = 10
chosen_word = random.choice(words.word_list).lower()
print(f"The chosen word is: {chosen_word}")

display = ["\U0001FA77" for _ in range(len(chosen_word))]
print(" ".join(display))

guessed_letters = []

game_over = False
while not game_over:
    guess = input("Guess a letter or the full word: ").lower()
    clear_screen()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    if len(guess) == 1:  # Guessing a single letter
        guessed_letters.append(guess)
        letter_guessed = False
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
                letter_guessed = True
        print(" ".join(display).upper())
        if not letter_guessed:
            attempts -= 1
            print("Incorrect guess. \nYou have", attempts, "attempts left.")  
    else:  # Guessing the whole word
        if guess == chosen_word:
            display = list(chosen_word)
        else:
            attempts -= 1
            print("Incorrect guess. \nYou have", attempts, "attempts left.")

    # print(" ".join(display).upper())

    if "\U0001FA77" not in display:
        game_over = True
        print("Congratulations! You guessed the word:", chosen_word)
    
    if attempts == 0:
        game_over = True
        print("Out of attempts. \nThe word was:", chosen_word)

    print(stages.stages[attempts])