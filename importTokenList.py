import sys
def import_token_list():
    token_list = [line.rstrip('\n') for line in open(sys.argv[3], 'r')]
    return token_list
    
