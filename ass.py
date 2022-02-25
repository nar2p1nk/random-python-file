import random
import time
def computeGuess(b):
    low = 1
    high = b
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"is {guess} high,low or correct? [h\\L/C]: ").lower()
        #print(f'{low},{high}')
        if feedback == 'l':
            low = guess - 1
        elif feedback == 'h':
            high = guess + 1

    print('i win')
    time.sleep(1)
    print('you lose')

computeGuess(100)

# secret number is 7
