def main():
    string = read() #SRYU
    vector[string] = tokenize(string) #SRYU
    escape_html(vector) #HANG
    apostrophe_lookup(vector) # you're -> you are SRYU
    standardlize(vector) #loooooove->love #HANG
    sanitize(vector) #remove @ # urladdr punctuation stop-words expression HANG/SRYU
    split_attach_word(vector) # displayisawesome -> display is awsome #HANG
    slang_replacement(vector) # u->you #SRYU





if __name__ == '__main__':
    main();