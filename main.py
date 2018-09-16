import random
import time


def draw():
    pass


def dice_roll():
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


def main():
    # time.sleep(1)
    print('Hello there.')
    # time.sleep(2)
    print('Would you like to play Disc Golf Dice?')

    yn = str(input('Y/N: '))

    if yn == 'n' or yn == 'N':
        print('Ok. Your loss! See ya.')
    elif yn == 'y' or yn == 'Y':
        dice_roll()
    else:
        print('Try typing "y or n"')
        main()


def place():
    pass


def score():
    pass


if __name__ == '__main__':
    main()
