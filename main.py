from escapeHtmlUtf8 import escape_html_utf8
from standardize import standardize

def main():    
    # string = read() #SRYU
    # escape_html_utf8(string) #HANG
    # vector[string] = tokenize(string) #SRYU
    # normalize(vector) # looked->look looks->look Look->look SRYU
    # standardize(vector) #loooooove->love #HANG
    # sanitize(vector) #remove @ # urladdr punctuation stop-words expression HANG/SRYU
    # slang_replacement(vector) # u->you #SRYU
    string = "I luv my <3 iphone & you're awsm apple. DisplayIsAwesome, sooo happppppy http://www.apple.com"
    escape_html_utf8(string)
    vec_str = [];
    vec_str.append('soooo')
    vec_str.append('happppppy')
    standardize(vec_str)
    split_attach_word(vec_str)
    print vec_str


if __name__ == '__main__':
    main();