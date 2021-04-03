from words import words
import random
import string
import time

def guess_the_word(word):
    guess = input('\n\nGuess the word: ').upper()
    if guess == word:
        print('You won! The word is: ', word)
    else:
        print('You lost! The word is: ', word)

def get_random_word():
    random_word = random.choice(words)
    # if the word contains '-' or two words is received, keep looking for 1 single word
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words)
    # then return the single word as the word to be guessed
    return random_word.upper()

def play():
    the_word = get_random_word()
    used_letters = set() # user guess without repetition
    words_letter = set(the_word) # letters in the words to be guessed without repetition
    alphabet = set(string.ascii_uppercase)
    lives = 6
    while len(words_letter) > 0:
        time.sleep(1)
        if lives <= 0:
            guess_the_word(the_word)
            return

        # print the letters user used in formatted version(eg. a b c d)
        print('\nLetters you used: ', ' '.join(used_letters))

        # create a list containing the word formatted with '_'
        word_list = [letter if letter in used_letters else '_' for letter in the_word]

        # print the letters in the word in string version
        print('To be guessed: ', ''.join(word_list))
        # print the current lives user have
        print('Lives left: ', lives)

        # get input from the user
        inp_letter = input('Guess a letter from the word: ').upper()

        # if the user's guess is not yet been used, add it to the used_letters set
        if inp_letter in alphabet - used_letters:
            used_letters.add(inp_letter)

            # if the user's guess is in the word to be guessed, remove the letter from word_letters set
            if inp_letter in words_letter:
                words_letter.remove(inp_letter)

            # if not, subtract 1 from lives
            else:
                lives -= 1

        # if the user already used same letter, just print something and do nothing
        elif inp_letter in used_letters:
            print('You already used this letter: \n')

        # if the input is not a character
        else:
            print('Invalid\n')

    # if it came down up to this point, it means the user guessed the word!
    print('\nYou won!\nThe word is: ', the_word)


if __name__ == '__main__':
    play()
