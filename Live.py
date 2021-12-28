from CurrencyRouletteGame import currency_roulette_game
from get_input_num import get_input_inum
from MemoryGame import memory_game
from GuessGame import guess_game
from requests import post


def welcome(name: str):
    return f"Welcome {name} to the World of Games (WoG). \n Here you can find many new ways to play."


# print(welcome("lena"))

def load_game(name: str):
    choose_game_text = f"Please choose a game to play: \n" \
                       f" 1. Memory Game - a sequence of numbers will appear for 1 " \
                       f"second and you have to guess it back\n" \
                       f" 2. Guess Game - guess a number and see if you chose like the computer\n" \
                       f" 3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"
    choose_level_text = "Please choose game level from 1 to 5:"

    game_number = get_input_inum(3, choose_game_text, 'pick a number between 1 and 3\n')
    game_level = get_input_inum(5, choose_level_text, 'choose a number between 1 and 5\n')

    print(f"you chose game number {game_number} at level {game_level}")

    if game_number == 3:
        game_result = currency_roulette_game(game_level)
    elif game_number == 1:
        game_result = memory_game(game_level)
    elif game_number == 2:
        game_result = guess_game(game_level)

    if game_result == True:
        print('You win!')
        r = post("http://localhost:5001/scores",
                 data={"acct": name,
                       "score": game_level * 3 + 5},
                 )
    else:
        print('you lose :(')

    return [game_number, game_level, game_result]
