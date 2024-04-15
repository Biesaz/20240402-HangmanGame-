import os
import random
import stages
import words

def clear_screan() -> None:
    os.system('cls')
clear_screan()

attempts = 10

chosen_word = random.choice(words.word_list).lower()
print(f"The chosen word is: {chosen_word}")
print("Hello!")

display = []

for i in range(len(chosen_word)):
    display += "\U0001F913"
print(" ".join(display))

game_over = False

while not game_over:
    guess = input("Guess a letter or the full word: ").lower()
    clear_screan()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(" ".join(display).upper())
    
    if guess not in chosen_word:
        attempts -= 1
        print("Incorrect guess. \nYou have", attempts, "attempts left.")
        if attempts == 0:
            game_over = True
            print("Out of attempts. \nThe word was:", chosen_word)
    if "\U0001F913" not in display:
        game_over = True
        print("Congratulations! You guessed the word:", chosen_word)
    print(stages.stages[attempts])    