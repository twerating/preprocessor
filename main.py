from readfile import read_file
from escapeHtmlUtf8 import escape_html_utf8
from tokenizer import tokenize
from normalizer import normalize
from standardize import standardize
from sanitizer import sanitize
from formTokenDict import form_token_dict

def main(): 
    raw_string = read_file()
    raw_string = escape_html_utf8(raw_string)
    vec_str = tokenize(raw_string)
    vec_str = normalize(vec_str)
    vec_str = standardize(vec_str)
    vec_str = sanitize(vec_str)
    token_dict = form_token_dict(vec_str)
    print token_dict

if __name__ == '__main__':
    main();
