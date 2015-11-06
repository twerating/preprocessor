import sys

def read_file():
    with open(sys.argv[1]) as raw_file:
        return raw_file.read().replace('\n', ' ')
