import HTMLParser

def escape_html_utf8(string):
    html_parser = HTMLParser.HTMLParser()
    string = string.decode("utf8").encode('ascii','ignore')
    string = html_parser.unescape(string)
    return string