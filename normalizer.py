from nltk.stem.wordnet import WordNetLemmatizer

def normalize(vec_token):
    lmtzr = WordNetLemmatizer()
    vec_token = [x.lower() for x in vec_token]
    vec_token = [lmtzr.lemmatize(x, 'v') for x in vec_token]
    return vec_token

vec = [u'Call', u'cAlLed', u'calls', u'calling', u'@sadh', u'123aisud128']

print normalize(vec)
