import datetime, random
from datetime import date

def main():
    #print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
        # 
        #
        #The Birthday Parasox shows us that in a group of N people, the odds 
        #that two of them have matching birthdays is surprisingly large.
        #This program does a Monte Carlo simulation (that is, repeated random 
        #simulations) to explore this concept.   
        #
        #(It's not actually a paradox, it's just a surprising result.)
        #''')
       
    ''' need to get number of birthdays to use to calculate percentage. must be an int'''
    while True:
        response = input('How many birthdays shall I generate? (Max 100)\n> ')
        try:
            num_birthdays = int(response)
            if 0 < num_birthdays <= 100:
                break
        except:
            print('Please enter a whole number between 1 and 100')
    # display numOfBirthdays birthdays
    birthday_list = getBirthdays(num_birthdays)
    formatted_birthday_list = [l.strftime('%b %d') for l in birthday_list]
    print(f'\nHere are {num_birthdays} birthdays:\n{formatted_birthday_list}')

    # check for matches
    if checkMatch(formatted_birthday_list):
        print(f'Multiple people have a birthday on: {checkMatch(formatted_birthday_list)}')
    else:
        print('There are no matching birthdays.')
    
    # run through 100,000 simulations
    input(f'Running 100,000 simualtions of {num_birthdays} birthdays.\n Press enter to begin! ')
    # keep count of  simulations with a match
    match_counter = 0
    for _ in range(100_000):
        birthday_list = getBirthdays(num_birthdays)
        if checkMatch(birthday_list):
            match_counter += 1
    probability = round(match_counter / 100_000 * 100, 2)
    print(f'There is a {probability}% chance of a group of {num_birthdays} people having at least one matching birthday!')
        


def getBirthdays(n):
    ''' create a list of birthdays '''
    birthdays = []
    # year is irrelevant, only days matter. start at jan 1
    for num in range(n):
        start = datetime.date(2025, 1, 1)
        # add random number of days to start of year (from 0-364)
        randomBirthday = start + datetime.timedelta(random.randint(0, 364))
        birthdays.append(randomBirthday)
    return birthdays

def checkMatch(x):
    matches = []
    # set(birthdays) will eliminate duplicates, which are matches in this instance
    if len(x) == len(set(x)):
        return None
    # run through list of birthdays and find the duplicates
    for a, birthdayA in enumerate(x):
        for b, birthdayB in enumerate(x[a+1 :]):
            if birthdayA == birthdayB:
                matches.append(birthdayA)
    return matches
                
if __name__ == '__main__':
    main()
    