from stop_words import get_stop_words




def sanitize(vec_token):
   stop_words = get_stop_words('en')
   return [x for x in vec_token if x not in stop_words];


print sanitize();
