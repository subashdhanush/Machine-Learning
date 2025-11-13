import random
import time
import os

def memory_test():
    words = ['apple', 'banana', 'grape', 'orange', 'lemon', 'mango', 'peach']
    selected = random.sample(words, 5)
    print("Memorize these words:")
    print(selected)
    time.sleep(5)

    # Clear screen (works for most systems)
    os.system('cls' if os.name == 'nt' else 'clear')

    recalled = []
    for i in range(5):
        word = input(f"Enter word {i+1}: ")
        recalled.append(word)

    correct = [w for w in recalled if w in selected]
    print(f"You remembered {len(correct)} correctly: {correct}")

memory_test()
