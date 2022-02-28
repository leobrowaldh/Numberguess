#!/usr/bin/env python3

import random


def guess(max_random_number, max_guesses):
    """Make you guess a random number the computer selects, given a max_random_number as the highest
    possible pick, and for a given number of maximum guessing attempts."""
    number = random.randrange(1, max_random_number + 1, 1)
    guessed_number = int(input(f'What number am i thinking?\nYou have {max_guesses} guesses\n '
                               f'HINT: number between 1 and {max_random_number}\n\n'))
    max_guesses -= 1
    while max_guesses > 0 and guessed_number != number:
        if guessed_number > number:
            print('You are guessing too high!')
            guessed_number = int(input(f'Try again\n{max_guesses} guesses left.\n\n'))
            max_guesses -= 1
        else:
            print('You are guessing too low!')
            guessed_number = int(input(f'Try again\n{max_guesses} guesses left.\n\n'))
            max_guesses -= 1
    if guessed_number == number:
        print('YES!\nHere is a cookie for you.')
    else:
        print('You failed!\nSo sorry')


if __name__ == "__main__":
    guess(10, 3)
