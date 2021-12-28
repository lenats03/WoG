from random import randint
from get_input_num import get_input_inum
def guess_game(level):
    secret_number=randint(1,level)
    print (secret_number)
    user_guess=get_input_inum(level,f'guess a number, from 1 to {level}','just a number please')
    return secret_number==user_guess