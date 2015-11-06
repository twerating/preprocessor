from nltk.stem.wordnet import WordNetLemmatizer

# called -> call
def normalize(vec_token):
    lmtzr = WordNetLemmatizer()
    vec_token = [x.lower() for x in vec_token]
    vec_token = [lmtzr.lemmatize(x, 'v') for x in vec_token]
    return vec_token
