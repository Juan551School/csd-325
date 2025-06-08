# Juan Macias Vasquez
# Date 06/08/2025
# Module 3.2 chohan_JCMV
"""Cho-Han Modified, by Juan Carlos Macias Vasquez

Modified version with 12% house fee and 10 mon bonus on rolling 2 or 7.
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, Modified by Juan Carlos Macias Vasquez

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

**If the dice roll totals 2 or 7, you get a 10 mon bonus!**
''')

purse = 5000

while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('JCMV: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor and asks for your bet.')
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('JCMV: ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine CHO or HAN
    rollIsEven = total % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Apply bonus if total is 2 or 7
    if total == 2 or total == 7:
        print(f"You rolled a total of {total}! You get a 10 mon bonus.")
        purse += 10

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        fee = int(pot * 0.12) # 12% house cut
        print('The house collects a', fee, 'mon fee.')
        purse -= fee
    else:
        purse -= pot
        print('You lost!')

    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
