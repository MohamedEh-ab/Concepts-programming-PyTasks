# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:50:05 2024

@author: Moham
"""
#random.shuffle, random.int
#list
#while, for in range(6)
#try and except?

import random
words = ['apple', 'pyramid', 'bonus', 'guava', 'astonishing', 'extraordinary', 'spiderman']
chosen_word = words[random.randint(0, len(words)-1)]
word = list(chosen_word)
random.shuffle(word)
guessed_word = ''.join(word)

print(f''' Welcome to the Word Scramble Game!
\nTry to guess the original word from the scrambled word: {guessed_word}
\nYou have 5 attempts.''')

for i in range(5):
    guessed = input("Enter your guess: ")
    # invalid
    if guessed == '' or guessed.isnumeric() or not guessed.isalpha():
        print("ERROR: input is invalid, commencing termination . . .")
        break
    # == 
    if guessed == chosen_word:
        print("Congratulations! You guessed the correct word!")
        break
    # !=
    elif guessed != chosen_word and i != 4:
        print(f" Incorrect! Try again. You have {4-i} attempts left.")
        continue
    # i = 4
    elif guessed != chosen_word and i == 4:
        print(f"You’re out of attempts! The correct word was: {chosen_word}")
        break