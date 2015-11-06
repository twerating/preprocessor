from itertools import groupby
import enchant

def standardize(vec_str):
    is_english = enchant.Dict("en_US")
    length = len(vec_str)
    for i in range(0, length):
        string = ''.join(''.join(s)[:2] for _, s in groupby(vec_str[i]))
        if not is_english.check(string):
            string = ''.join(''.join(s)[:1] for _, s in groupby(vec_str[i]))
        if is_english.check(string):
            vec_str[i] = string
    return vec_str