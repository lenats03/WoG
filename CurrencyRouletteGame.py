from requests import get
import re
from get_input_num import get_input_inum

def currency_roulette_game(level):
    ratexml = get('https://www.boi.org.il/currency.xml?curr=01').text
    rate = float(re.search('<RATE>.*</RATE>', ratexml).group().strip('RATE<>/'))
    orig_amt=get_input_inum(1000000000000, 'enter the amount of NIS to convert ', 'just a number please ', typen=float)

    fails_no=0
    while True :
        converted_amt=get_input_inum(1000000000000, f'guess how much is it worth in USD \n you have {level} attempts ', 'just a number please ', typen=float)
        if abs(converted_amt-orig_amt*rate) <level:
            return True
        else:
            fails_no=fails_no+1
            if fails_no>=level:
                return False



