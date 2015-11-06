from nltk.tokenize import TweetTokenizer

def tokenize(raw_string):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(raw_string);
