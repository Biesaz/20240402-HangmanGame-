import os
import random
import stages
import words
from typing import List

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

    def play_game(self) -> None:
        self.clear_screen()
        # print(f"The chosen word is: {self.chosen_word}") # trinti
        self.display_word()

        while not self.game_over:
            guess = input("Guess a letter or the full word: ").lower()
            self.clear_screen()

            if guess in self.guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            if len(guess) == 1:  # Guessing a single letter
                self.guessed_letters.append(guess)
                letter_guessed = self.update_display(guess)
                self.display_word()
                if not letter_guessed:
                    self.attempts -= 1
                    print("Incorrect guess. \nYou have", self.attempts, "attempts left.")
            else:  # Guessing the whole word
                if guess == self.chosen_word:
                    self.display = list(self.chosen_word)
                else:
                    self.attempts -= 1
                    print("Incorrect guess. \nYou have", self.attempts, "attempts left.")

            if "\U0001FA77" not in self.display:
                self.game_over = True
                print("Congratulations! You guessed the word:", self.chosen_word)
            if self.attempts == 0:
                self.game_over = True
                print("Out of attempts. \nThe word was:", self.chosen_word)
            print(stages.stages[self.attempts])

if __name__ == "__main__":
    game = HangmanGame()
    game.play_game()