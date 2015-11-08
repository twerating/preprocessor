from preprocess import preprocess
import sys

def form_token_list(vec_token):
    token_dict = dict()
    for token in vec_token:
        if token in token_dict:
            token_dict[token] = token_dict[token] + 1
        else:
            token_dict[token] = 0

    return [token for token in token_dict if [token_dict] > 5]

def main():
	in_file = open(sys.argv[1], 'r')
	out_file = open(sys.argv[2], 'w')
	raw_string = in_file.read().replace('\n', ' ')
	vec_token = preprocess(raw_string)
	token_list = form_token_list(vec_token)

	for token in token_list:
		out_file.write(token + '\n')

if __name__ == '__main__':
	main()
