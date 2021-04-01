import random
import timeit

def guess_by_computer(r, correct_num):
    low = 0
    high = r
    guess = 0
    tries = 0

    while guess != correct_num:
        # if range is not up to 1
        if low != high:
            guess = random.randint(low, high)
        elif low == high:
            guess = low = high
            break

        # if the guess is lower than the correct number,
        if correct_num > guess:
            low = guess + 1         # set low to be limit to be (guess + 1, high)

        # if guess is high than the correct number,
        elif correct_num < guess:
            high = guess - 1        # set the limit to be (low, guess - 1)

        tries += 1

    print(f"After {tries} tries, the computer figured the user's number. It is {guess}.")


if __name__ == '__main__':
    time_exec = timeit.default_timer()
    to_guess = int(input('Enter a valid integer that will be guessed by the computer: '))
    guess_by_computer(1000, to_guess)
    print(f'Time execution: {time_exec} seconds')


