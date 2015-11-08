from stop_words import get_stop_words
import enchant
import string

def sanitize(vec_token):
    is_english = enchant.Dict("en_US")
    stop_words = get_stop_words('en')
    vec_token = [x for x in vec_token if x not in stop_words];
    vec_token = [x for x in vec_token if ('@' not in x and '#' not in x)]
    vec_token = [x for x in vec_token if x.isalpha()]
    vec_token = [x for x in vec_token if is_english.check(x)]
    exclude = set(string.punctuation)
    vec_token = [x for x in vec_token if x not in exclude]
    return vec_token
