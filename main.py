from readfile import read_file
from escapeHtmlUtf8 import escape_html_utf8
from tokenizer import tokenize
from normalizer import normalize
from standardize import standardize
from sanitizer import sanitize

def main(): 
    raw_string = read_file()
    raw_string = escape_html_utf8(raw_string)
    vec_str = tokenize(raw_string)
    vec_str = normalize(vec_str)
    vec_str = standardize(vec_str)
    vec_str = sanitize(vec_str)
    print vec_str

if __name__ == '__main__':
    main();