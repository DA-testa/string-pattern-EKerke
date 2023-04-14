# python3
import sys

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    in_type = input().strip().lower()
    if in_type == 'f':
        path = input().strip()
        with open(path, 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()

    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output))) 

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    m = len(pattern)
    n = len(text)
    p = 31
    q = 10**9+7
    h_pattern = 0
    for i in range(m):
        h_pattern = (h_pattern * p + ord(pattern[i])) % q

    h_text = [0] * (n - m + 1)
    h_text[0] = 0
    for i in range(m):
        h_text[0] = (h_text[0] * p + ord(pattern[i])) % q
    print('h_text[0]:', h_text[0])
    for i in range(1, n - m + 1):
        h_text[i] = ((h_text[i-1] - ord(text[i-1]) * pow(p, m-1, q)) * p + ord(text[i+m-1])) % q
        print('h_text[{}]:'.format(i), h_text[i])

    position = []
    for i in range(n - m + 1):
        if h_text[i] == h_pattern:
            if text[i:i+m] == pattern:
                position.append(i)

    # and return an iterable variable
    print('position:', position)
    return position


# this part launches the functions
if __name__ == '__main__':
    try: 
        print_occurrences(get_occurrences(*read_input())) 
    except EOFError: 
        sys.exit(1) 

