import sys
import re

def read_input():
    """Reads a series of strings separated by \n and returns a list.
    """
    output = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        output.append(line.strip())
    return output

def is_valid_url(url: str) -> bool:
    return re.match(r"http(s?):\/\/[A-Za-z0-9\-\.\_\~\:\/\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\%\=]+", url) is not None        