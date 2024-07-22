import os
import random

def get_word():
    word = ''
    
    with open(os.getcwd() + '\\Wordle\\words.txt','r') as file:
    # for line in file.readlines():
    #     print(line)
        words = file.readlines();

        randomNumber = random.randint(0, len(words))
        word = words[randomNumber]

        #temp
        print(word)
    return word




def get_guess():
    guess = ''    
    playerGuess = print("What is your guess?:")

    while len(guess) != 5:
        guess = input()

    return guess



def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
    word_guessed = len(misplaced_letters) == 0 and len(wrong_letters) == 0
    return word_guessed



if __name__ == '__main__':
    word = get_word()
    word_guessed = False
    tries = 0
    while word_guessed == False and tries != 5:
        guess = get_guess()
        word_guessed = show_guess(guess, word)
        tries = tries + 1
    
    if tries == 5:
        print("You didnt guess the word! Unlucky!")    
    elif word_guessed == True:
        print("You guessed the word! Hurrah!")

