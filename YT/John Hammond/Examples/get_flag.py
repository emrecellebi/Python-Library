#!/usr/bin/env python2

import string;
import collections;
# https://www.youtube.com/watch?v=I6ElvNK6ZY0


def rotate(rotate_string, number_to_rotate_by):
#{
    upper = collections.deque(string.ascii_uppercase);
    lower = collections.deque(string.ascii_lowercase);
    
    upper.rotate(number_to_rotate_by);
    lower.rotate(number_to_rotate_by);
    
    upper = ''.join(list(upper));
    lower = ''.join(list(lower));
    
    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower));
#}

challenge_string = "";

def brute_force_cipher():
#{
    for i in range(len(string.ascii_uppercase)):
    #{
        print i, rotate(challenge_string, i);
    #}
#}

def get_answer():
#{
    return rotate(challenge_string, 12);
#}

def get_flag():
#{
    return get_answer().split()[-1];
#}

print get_flag();