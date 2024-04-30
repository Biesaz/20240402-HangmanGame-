import os
import random
import logging
import stages
import words
from typing import List

# Clearing the log file before the game starts
open('hangman.log', 'w').close()

logging.basicConfig(filename='hangman.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HangmanGame:
    def __init__(self) -> None:
        self.attempts: int = 10
        self.chosen_word: str = random.choice(words.word_list).lower()
        self.display: List[str] = ["\U0001FA77" for _ in range(len(self.chosen_word))]
        self.guessed_letters: List[str] = []
        self.game_over: bool = False
        
    def clear_screen(self) -> None:
        os.system('cls')

    def display_word(self) -> None:
        print(" ".join(self.display).upper())
        
    def update_display(self, guess: str) -> bool:
        letter_guessed: bool = False
        for position in range(len(self.chosen_word)):
            letter = self.chosen_word[position]
            if letter == guess:
                self.display[position] = guess
                letter_guessed = True
        return letter_guessed
    
    def validate_input(self, guess: str) -> bool:
        if guess in self.guessed_letters:
            output = "You already guessed that letter. Try again."
            print(output)
            logging.info(output)
            return False

        if len(guess) != 1 and len(guess) != len(self.chosen_word):
            output = "Please enter a single letter or the full word of correct length."
            print(output)
            logging.info(output)
            return False

        if not guess.isalpha():
            output = "Please enter only letters."
            print(output)
            logging.info(output)
            return False
        
        return True
    
    def check_game_state(self) -> None:
        if "\U0001FA77" not in self.display:
            self.game_over = True
            output = "Congratulations! You guessed the word: {}".format(self.chosen_word)
            print(output)
            logging.info(output)
        elif self.attempts == 0:
            self.game_over = True
            output = "Out of attempts. \nThe word was: {}".format(self.chosen_word)
            print(output)
            logging.info(output)
    
    def play_game(self) -> None:
        self.clear_screen()
        self.display_word()

        while not self.game_over:
            print("\nGuessed Letters:", ", ".join(self.guessed_letters))
            print("Attempts Remaining:", self.attempts)
            guess = input("Guess a letter or the full word: ").lower()
            logging.info(f"Guessed input: {guess}")
            self.clear_screen()
            
            if not self.validate_input(guess):
                continue

            if len(guess) == 1:  # Guessing a single letter
                self.guessed_letters.append(guess)
                letter_guessed = self.update_display(guess)
                self.display_word()
                if not letter_guessed:
                    self.attempts -= 1
                    output = "Incorrect guess. \nYou have {} attempts left.".format(self.attempts)
                    print(output)
                    logging.info(output)
            else:  # Guessing the whole word
                if guess == self.chosen_word:
                    self.display = list(self.chosen_word)
                else:
                    self.attempts -= 1
                    output = "Incorrect guess. \nYou have {} attempts left.".format(self.attempts)
                    print(output)
                    logging.info(output)

            self.check_game_state()
            print(stages.stages[self.attempts])

if __name__ == "__main__":
    game = HangmanGame()
    game.play_game()