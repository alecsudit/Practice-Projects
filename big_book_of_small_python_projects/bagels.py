# need to update this to be able to tolerate letters, leading 0s, etc. 

'''
BAGELS --> must guess a secret 3 digit number in 10 tries
    Hints:
    'Pico' = guess has a correct digit in the wrong place 
    'Fermi' = guess has correct digit in correct place
    'Bagels' = guess has no correct digits
'''

import random

intro = 'Bagels, a deductive logic game.\n' \
'By Al Sweigart al@inventwithpython.com\n\n' \
'I am thinking of a 3-digit number. Try to guess what it is.\n' \
'Here are some clues:\n' \
'When I say:    That Means:\n' \
'Pico (1)          One digit is correct but in the wrong position.\n' \
'Fermi (1)         One digit is correct and in the right position.\n' \
'Bagel             No digit is correct.\n' \
'I have thought up a number.\n' \
'You have 10 guesses to get it.\n' \

def main():
    print(intro)
    num_of_digits = 3
    max_guesses = 10
    secret_number = str(generate_rand_int(num_of_digits))
    print(secret_number)
    game = guessing(secret_number, max_guesses)
    print(game)


def generate_rand_int(n):
    end_range = int('9'*n)
    rand_int = random.randint(0, end_range)
    return rand_int

def guessing(sn, max):
    trial = 1
    while trial <= max:
        print(f'Guess #{trial}:')
        guess = input('> ')
        if len(guess) != len(sn):
            print(f'Your guess needs to be a {len(sn)}-digit number!')
            trial += 1
            continue
        else:
            pico = 0
            fermi = 0
            if guess == sn:
                return('You got it!')
            for g in range(len(guess)):
                if guess[g] in sn:
                    if guess[g] == sn[g]:
                        fermi += 1
                    else:
                        pico += 1
            if pico + fermi == 0:
                print('Bagel')
            if pico > 0:
                print(f'Pico({pico})')
            if fermi > 0:
                print(f'Fermi({fermi})')
            trial += 1
    return ('You ran out of guesses! The correct answer was {sn}')





if __name__ == '__main__':
    main()