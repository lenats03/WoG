import Utils
from time import sleep
from get_input_num import get_input_inum

from random import randint


def memory_game(level):
    nums = []
    for i in range(level):
        nums.append(randint(1, 101))
    print('Memorize the numbers: ', nums)
    sleep(1)

    Utils.clean_screen()
    guessed_nums = []
    for i in range(level):
        num=get_input_inum(101, f'guess the {i+1} number ', 'just a number')
        guessed_nums.append(num)
        print (sorted(guessed_nums),sorted(nums))
    return sorted(guessed_nums)==sorted(nums)


