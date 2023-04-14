# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    in_type = input().rstrip().lower()
    if in_type == 'f':
        path = input().rstrip()
        with open(path, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()

    
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
    h_pattern = 0
    for i in range(m):
        h_pattern = (h_pattern * p + ord(pattern[i])) % 10**9+7

    h_text = [0] * (n - m + 1)
    h_text[0] = 0
    for i in range(m):
        h_text[0] = (h_text[0] * p + ord(pattern[i])) % 10**9+7
    for i in range(1, n - m + 1):
        h_text[i] = ((h_text[i-1] - ord(text[i-1]) * pow(p, m-1, 10**9+7)) * p + ord(text[i+m-1])) % 10**9+7

    pozition = []
    for i in range(n - m +1):
        if h_text[i] == h_pattern:
            if text[i:i+m] == pattern:
                pozition.append(i)

    # and return an iterable variable
    return pozition


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

