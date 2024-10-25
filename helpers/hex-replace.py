from typing import List


def hex_clean(input_string: str) -> str:
    input_string_list: List[str] = input_string.split(' ')

    result: List[str] = []
    for i, word in enumerate(input_string_list):
        if word == "(hex)":
            result[-1] = str(int(result[-1], 16))
        else:
            result.append(word)
    return result
