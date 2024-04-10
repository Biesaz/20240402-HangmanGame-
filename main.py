import os
import random
import stages
import words

def clear_screan() -> None:
    os.system('cls')    

def choose_word(word_list: list[str]) -> str:
    return random.choice(word_list)

chosen_word = choose_word(words.word_list)
# print(f"The chosen word is: {chosen_word}")

def hangman_game(word: str, max_attempts: int = 10) -> None:
    guessed_word = ['\U0001F913'] * len(word)
    attempts = max_attempts
    clear_screan()
    
    while attempts > 0 and '\U0001F913' in guessed_word:
        print(" ".join(guessed_word))
        guess = input("Guess a letter or the full word: ").upper()[0]
        clear_screan()

        if len(guess) == 1:  # Guess is a letter
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
                print("Correct!" )
    
            else:
                attempts -= 1
                print("Incorrect guess. You have", attempts, "attempts left.")
                if attempts > 0:
                    print(stages.stages[max_attempts - attempts - 1])
                else:
                    print(stages.stages[max_attempts])
        else:  # Guess is the full word
            if guess == word:
                guessed_word = list(word)
            else:
                attempts -= 1
                print("Incorrect guess. You have", attempts, "attempts left.")
        # print(stages.stages[attempts])
        if attempts < len(stages.stages):
            print(stages.stages[attempts])
        else:
            print("Out of attempts. The word was:", word)
    if '\U0001F913' not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of attempts. The word was:", word)

    # print(stages.stages[attempts])    

hangman_game(chosen_word)