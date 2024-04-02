import random

possible_words = word_list = [
    "Apple",
    "Banana",
    "Computer",
    "Elephant",
    "Guitar",
    "Sunshine",
    "Mountain",
    "Football",
    "Butterfly",
    "Library",
    "Rainbow",
    "Dragon",
    "Pizza",
    "Bicycle",
    "Adventure",
    "Chocolate",
    "Fireworks",
    "Telescope",
    "Watermelon",
    "Vacation"
]

def choose_word(word_list: list[str]) -> str:
    return random.choice(word_list)

chosen_word = choose_word(possible_words)
print(f"The chosen word is: {chosen_word}")