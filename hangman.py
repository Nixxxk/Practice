import random
word_list = ["apple","beautiful","potato"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in range(len(chosen_word)): # 0 1 2 3 4 5 
    display += '_'
print(display)
game_over=False
while not game_over:

    guessed_letter = input("Guess a letter: ")
    for letter  in chosen_word:
        if letter==guessed_letter:
            print("Matched")
        else:
            print("Not matched")