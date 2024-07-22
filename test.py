if __name__ == '__main__':
    word = get_word()
    word_guessed = False
    tries = 0
    while word_guessed == False or tries != 5:
        guess = get_guess()
        word_guessed = show_guess(guess, word)
        tries = tries + 1
    if word_guessed:
        print("You guessed the word! Hurrah!")
    else:
        print("You didnt guess the word! Unlucky!")