import sys
import HTMLParser
from nltk.tokenize import TweetTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from itertools import groupby
import enchant
from stop_words import get_stop_words
import enchant
import string

'''
	Escaping HTML encoding text & convert utf8 to ascii
'''
def escape_html_utf8(string):
    html_parser = HTMLParser.HTMLParser()
    string = string.decode("utf8").encode('ascii','ignore')
    string = html_parser.unescape(string)
    return string

'''
	Tokenize raw tweets to list of token
'''
def tokenize(raw_string):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(raw_string);

'''
	Normalize different form of words and convert to lowercases for example
	Called -> call
	teEth -> tooth
'''
def normalize(vec_token):
    lmtzr = WordNetLemmatizer()
    vec_token = [x.lower() for x in vec_token]
    vec_token = [lmtzr.lemmatize(x, 'v') for x in vec_token]
    vec_token = [lmtzr.lemmatize(x, 'n') for x in vec_token]
    return vec_token

'''
	Standardize repeated letters
	Loooooove -> love
'''
def standardize(vec_token):
    is_english = enchant.Dict("en_US")
    length = len(vec_token)
    for i in range(0, length):
        string = ''.join(''.join(s)[:2] for _, s in groupby(vec_token[i]))
        if not is_english.check(string):
            string = ''.join(''.join(s)[:1] for _, s in groupby(vec_token[i]))
        if is_english.check(string):
            vec_token[i] = string
    return vec_token

'''
	Sanitize tokens. Following type of tokens will be removed
	1. stop_words
	2. Hashtag(#abc)
	3. Namelink(@abc)
	4. Contains non letter words
	5. Punctuation
'''
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

'''
	Convert raw string to vector of preprocessed tokens
'''
def preprocess(raw_string):
    raw_string = escape_html_utf8(raw_string)
    vec_token = tokenize(raw_string)
    vec_token = normalize(vec_token)
    vec_token = standardize(vec_token)
    vec_token = sanitize(vec_token)
    return vec_token
