#!/usr/bin/env python3

import random
from time import sleep


def pc_guess(min_number, max_number):
    number = random.randrange(min_number, max_number + 1, 1)
    print('...')
    print('Let\'s see........')
    sleep(random.randrange(1, 5, 1))
    answer = input(f'Is it {number}? (y/n)\n')
    # loop until the answer is 'y':
    while answer != 'y':
        answer = input('Did I guess too low or too high? (low/high)?\n')
        # if pc guessed too low, we make the new min_number the number following the guessed number.
        if answer == 'low':
            min_number = number + 1
            number = random.randrange(min_number, max_number + 1, 1)
            answer = input(f'Is it {number}? (y/n)\n')
            # let's continue to see if pc guessed too high or low this time...
            continue
        # if pc guessed too high, we make the new max_number the number preceding the guessed number.
        elif answer == 'high':
            max_number = number - 1
            number = random.randrange(min_number, max_number + 1, 1)
            answer = input(f'Is it {number}? (y/n)\n')
            # let's continue to see if pc guessed too high or low this time...
            continue
        # If user don't give the expected answer:
        else:
            print(f'What did you say? is {number} lower or higher than the number you are thinking?')
    # At this point, the answer has to be 'y'
    print('Gotya!!! :D\n')


if __name__ == "__main__":
    print('Think a secret number...')
    print('...')
    sleep(3)
    # Obtaining a tuple of min,max integers from the user:
    user_range = list(input('Now give me a range to guess. (min_number,max_number)\n').split(','))
    user_range = tuple(map(int, user_range))
    min_n, max_n = user_range
    # try the pc_guess function and continue unless the user give contradictory input.
    try:
        pc_guess(min_n, max_n)
    except ValueError:
        print('You are messing around, I don\'t have time for this.')