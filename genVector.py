from preprocess import preprocess
import sys

def form_token_dict(vec_token):
    token_dict = dict()
    for token in vec_token:
        if token in token_dict:
            token_dict[token] = token_dict[token] + 1
        else:
            token_dict[token] = 0

    return token_dict

def main():
    in_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')
    token_list = import_token_list()
    raw_string = in_file.read().replace('\n', ' ')
    vec_token = preprocess(raw_string)
    token_dict = form_token_dict(vec_token)
    vector = gen_vector(token_dict, token_list)
    for item in vector:
        out_file.write(str(item) + ' ')

def import_token_list():
    token_list = [line.rstrip('\n') for line in open(sys.argv[3], 'r')]
    return token_list

def gen_vector(token_dict, token_list):
    vector = []
    for token in token_list:
        if token in token_dict:
            vector.append(token_dict[token])
        else:
            vector.append(0)
    return vector

if __name__ == '__main__':
    main()
