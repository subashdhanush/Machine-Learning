import random

def word_scramble():
    words = ["python", "developer", "challenge", "keyboard", "algorithm"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    
    print(f"Unscramble this word: {scrambled}")
    guess = input("Your guess: ")

    if guess.lower() == word:
        print("Correct! 🎉")
    else:
        print(f"Oops! The correct word was: {word}")

word_scramble()
