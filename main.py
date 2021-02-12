import sys

def read_input():
    """Reads a series of strings separated by \n and returns a list.
    """
    output = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        output.append(line.strip())
    return output    