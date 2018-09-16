import random
import time


def draw():
    pass


def place():
    pass


def roll():
    blue = random.randint(1, 6)
    red = random.randint(1, 6)
    green = random.randint(1, 6)
    yellow = random.randint(1, 6)

    print('You rolled: ')
    print()
    print('Blue: ' + str(blue))
    print('Red: ' + str(red))
    print('Green: ' + str(green))
    print('Yellow: ' + str(yellow))


def score():
    pass


def main():
    time.sleep(1)
    print('Hello there.')
    time.sleep(2)
    print('Would you like to play Disc Golf Dice?')
    yn = str(input('Y/N: '))

    if yn == 'y' or 'Y':
        roll()
    elif yn == 'n' or 'N':
        print('Ok. Your loss! See ya.')
    else:
        print('Try typing "y or n"')


if __name__ == '__main__':
    main()
