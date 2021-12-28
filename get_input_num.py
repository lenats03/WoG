def get_input_inum(max_num, text1, text2, typen=int):
    while True:
        try:
            input_int = typen(input(text1))
            assert 1 <= input_int <= max_num
            break
        except AssertionError:
            print(text2 + "\n")
            continue
        except TypeError:
            print(text2 + "\n")
            continue
        except ValueError:
            print(text2 + "\n")
            continue
    return input_int