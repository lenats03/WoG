from os import system

SCORES_FILE_NAME = 'scores.txt'
BAD_RETURN_CODE = 1


def clean_screen():
    system('cls')
    return 0
