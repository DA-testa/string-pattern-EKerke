# python3
import sys

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    in_type = input().rstrip().lower()
    if in_type == 'f':
        path = input().rstrip()
        with open(f"./tests/{path}") as f:
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
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output))) 

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    m = len(pattern) 
    n = len(text) 
    p = 31 # a prime number for hashing 
    q = 10**9+9 
    h = p ** (m - 1) % (10**9+9) 
    h_pattern = 0 
    h_text = 0 
    position = [] 

    for i in range(m): 
        h_pattern = (h_pattern * p + ord(pattern[i])) % q 
        h_text = (h_text * p + ord(text[i])) % q  
        
    for i in range(n - m + 1): 
        if h_pattern == h_text and text[i:i+m] == pattern: 
            position.append(i) 
        if i < n - m: 
            h_text = (h_text - ord(text[i]) * h) % q 
            h_text = (h_text * p + ord(text[i + m])) % q 

    # and return an iterable variable
    return position


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input())) 
    

