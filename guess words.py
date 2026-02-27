import random

words = ["apple", "mango", "grapes", "chair", "table",
         "phone", "water", "light", "plant", "bread"]

word = random.choice(words)
scrambled = "".join(random.sample(word, len(word)))

print("Scrambled word:", scrambled)

for i in range(3):
    guess = input("Guess the word: ")
    
    if guess == word:
        print("Correct! You win 🎉")
        break
    else:
        print("Wrong! Try again.")
else:
    print("Out of attempts! The word was:", word)
