import random
import sys
import os
#import argparse

# random.SystemRandom() should be cryptographically secure
try:
    rng = random.SystemRandom
except AttributeError:
    sys.stderr.write("WARNING: System does not support cryptographically "
                     "secure random number generator or you are using Python "
                     "version < 2.4.\n"
                     "Continuing with less-secure generator.\n")
    rng = random.Random

# Python 3 compatibility
if sys.version[0] == "3":
    raw_input = input


# Set up variables.
num = 8884 # Wordlist is 8884 words.
fileloc = os.path.expanduser('~/bin/python/Password_Generator/wordlist.txt')  # Open file.

 
# def der(*args):
#     if type(args) != int:
#         print('Invalid input.')


# Number of words.
HowMany = raw_input('How many words long? ')

# Generate random number that is between 1 and the length of the wordlist.
def rand():
    chosen = rng().randrange(1, num, 1)
    return(chosen) 
        


# Choose a word based the generated number:
# Use enumerate to select the lines, so the entire list isn't read into memory.
def grabber(linenum):
    with open(fileloc, 'r') as wordlist:
        for LineNumber, word in enumerate(wordlist):
            if LineNumber == linenum:
                return((word).replace('\n',''))
        

# Concatenate words into single string.
def buildit(length):
    x = 0
    password = []
    while x < length:
        word = grabber(rand())
        password.append(word)
        x += 1
    print(' '.join(password))
        

buildit(int(HowMany))
