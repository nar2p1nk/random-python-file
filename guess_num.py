import random
import time

def guess(b):
    print(f'the limit is {b}')
    randomNumber = random.randint(1, b)
    guess = 0
    while guess != randomNumber:
        guess = int(input('guess a number: '))

        if randomNumber > guess:
            print('higher')
            # guess = int(input('enter a number: '))
        elif randomNumber < guess:
            print('lower')
            # guess = int(input('enter a number: '))
        if guess > b:
            print(f'the limit is {b} idiot')

        
    print('congrats')


def guess_compute(b):
    low = 1
    high = b
    judgement = ''
    while judgement != 'y':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        print(guess)
        judgement =input('is this correct? [Y/n]: ').lower()

        if judgement == 'y':
            print('i win')
            time.sleep(2)
            print('you lose')
            time.sleep(2)
            break
        elif judgement == 'n':


            feedback = input('higher or lower? [H/l]: ')
            print(f'{low},{high}')

            if feedback == 'h':
                low = guess + 1
            elif feedback == 'l':
                high = guess - 1


guess_compute(1000)

# 420