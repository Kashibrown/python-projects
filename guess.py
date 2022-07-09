import random 

def user_guess(x):
    number = random.randint(1,x)
    guess = 0
    while guess != number:
        guess = int(input(f'Enter a number from 1 -- {x}: '))
        if guess < number :
            print('Too low, try again')
        elif guess > number:
            print('Too high, try again')
    print(f'Yay! you guessed the number {number} correctly!')
      
user_guess(10)

def computer_guess(x):
    low = 1
    high = x
    response = ''
    while response != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        response = input(f'Is {guess} too high(H) or too low(L) or correct(C): ').lower()
        if response == 'h':
            high = guess - 1
            print('too high!')
        if response == 'l':
            low = guess + 1
            print('too low!')
    print(f'Yay!, you guessed the number {guess} correctly!')
    
computer_guess(10)