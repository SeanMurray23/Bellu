DIGIT_MAP = {
    'zero': '0',
    'one' : '1',
    'two' : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six': '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'    
}

def converts(s):
    try:
        number =""
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        x = -1
    return x